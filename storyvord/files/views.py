from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FileSerializer, FolderSerializer
from .models import File, Folder
from project.models import Project
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

class FolderListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FolderSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, pk, format=None):
        user = request.user
        folders = Folder.objects.filter(
            Q(project=pk) & (Q(allowed_users=user) | Q(default=True))
        ).distinct()
        serializer = FolderSerializer(folders, many=True, context={'exclude_files': True})
        return Response(serializer.data)


    def post(self, request, pk, format=None):
        user = request.user

        project = get_object_or_404(Project, pk=pk)

        if project.user != user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        folder = Folder.objects.filter(project=pk, name=request.data.get('name'))
        if folder:
            return Response({"detail": "Folder with the same name already exists."}, status=status.HTTP_400_BAD_REQUEST)

        if 'default' in request.data:
            request.data.pop('default')

        data = request.data.copy()
        data['project'] = pk

         # Make sure the user who is creating the file is in the list of allowed
        allowed_users = data.getlist('allowed_users')
        if not allowed_users:
            allowed_users = [user.id]
        else:
            allowed_users.append(user.id)

        data.setlist('allowed_users', allowed_users)
            
        serializer = FolderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # add user to allowed users or remove user from allowed users
    
class FolderDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FolderSerializer
    
    def put(self, request, pk, format=None):
        user = request.user
        
        folder = get_object_or_404(Folder, pk=pk)
        
        if folder.project.user != user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        if 'default' in request.data:
            request.data.pop('default')
            
        if 'project' in request.data:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'message': 'You cannot change the project of a folder.'})
        
        # To ensure complete allowed_user doesnot get edited
        if 'allowed_users' in request.data:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'message': 'You cannot update allowed_users field. Use "add_users" and "remove_users" fields instead.'})

        # Add additional users if 'add_users' is provided in request
        if 'add_users' in request.data:
            add_users_ids = request.data.pop('add_users')
            for user_id in add_users_ids:
                folder.allowed_users.add(user_id)

        # Remove users if 'remove_users' is provided in request
        if 'remove_users' in request.data:
            remove_users_ids = request.data.pop('remove_users')
            for user_id in remove_users_ids:
                folder.allowed_users.remove(user_id)
        
        # Make sure the user who is updating the file is in the list of allowed
        if request.user not in folder.allowed_users.all():
            folder.allowed_users.add(request.user)

        serializer = FolderSerializer(folder, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FileListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)

    # Get the list of files in a folder
    def get(self, request, pk, format=None):
        folder = get_object_or_404(Folder, pk=pk)
        if not folder.allowed_users.filter(id=request.user.id).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)

        files = folder.files

        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        user = request.user

        folder = get_object_or_404(Folder, pk=pk)
        
        if not folder.project.user == user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # Check if the file with same name exists
        file = File.objects.filter(folder=pk, name=request.data.get('name'))
        if file:
            return Response({"detail": "File with the same name already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Make a mutable copy of request.data
        data = request.data.copy()
        data['folder'] = pk

        serializer = FileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FileSerializer

    # Get the details of a file
    def get(self, request, pk, format=None):
        file = get_object_or_404(File, pk=pk)

        # Who can view a file?
        if not file.folder.allowed_users.filter(id=request.user.id).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = FileSerializer(file)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        file = get_object_or_404(File, pk=pk)

        # Who can delete a file?
        if not file.folder.project.user == request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        file = get_object_or_404(File, pk=pk)

        # Who can update a file?
        if not file.folder.project.user == request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # Ensure the folder id doesnot change
        if 'folder' in request.data:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'message': 'You cannot change the folder of a file.'})

        serializer = FileSerializer(file, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


# Crew side file view 

class AccessibleFileListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        files = File.objects.filter(allowed_users=user)
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AccessibleFileDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        try:
            file = File.objects.get(pk=pk)
        except File.DoesNotExist:
            return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)

        if not file.allowed_users.filter(id=request.user.id).exists():
            return Response({"error": "You do not have permission to access this file."}, status=status.HTTP_403_FORBIDDEN)

        serializer = FileSerializer(file)
        return Response(serializer.data, status=status.HTTP_200_OK)