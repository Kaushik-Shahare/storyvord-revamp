
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import *
from .serializers import *
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from accounts.models import User

class ProjectListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        projects = Project.objects.filter(user=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise NotFound("Project not found")
        if project.user != user:
            raise PermissionDenied("You do not have permission to access this project")
        return project

    def get(self, request, pk):
        project = self.get_object(pk, request.user)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        project = self.get_object(pk, request.user)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk, request.user)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SendOnboardRequestAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, project_id, crew_id, *args, **kwargs):
        try:
            project = Project.objects.get(pk=project_id, user=request.user)
            crew = User.objects.get(pk=crew_id, user_type='crew')
            onboard_request = OnboardRequest.objects.create(project=project, crew=crew)
            return Response(OnboardRequestSerializer(onboard_request).data, status=status.HTTP_201_CREATED)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found or you are not authorized to send onboard requests for this project.'}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({'error': 'Crew member not found.'}, status=status.HTTP_404_NOT_FOUND)

class AcceptOnboardRequestAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, request_id, *args, **kwargs):
        try:
            onboard_request = OnboardRequest.objects.get(pk=request_id, crew=request.user, status='pending')
            onboard_request.status = 'accepted'
            onboard_request.save()
            onboard_request.project.selected_crew.add(request.user)
            return Response(OnboardRequestSerializer(onboard_request).data, status=status.HTTP_200_OK)
        except OnboardRequest.DoesNotExist:
            return Response({'error': 'Onboard request not found or already processed.'}, status=status.HTTP_404_NOT_FOUND)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found.'}, status=status.HTTP_404_NOT_FOUND)
        
class ListOnboardRequestsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.user_type == 'client':
            onboard_requests = OnboardRequest.objects.filter(project__user=request.user)
        elif request.user.user_type == 'crew':
            onboard_requests = OnboardRequest.objects.filter(crew=request.user)
        else:
            return Response({'error': 'Only clients and crew members can view onboard requests.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = OnboardRequestSerializer(onboard_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)