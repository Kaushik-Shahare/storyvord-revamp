from accounts.models import Country

countries_data = [
    ("Afghanistan", "AF", "AFG", "004"),
    ("Albania", "AL", "ALB", "008"),
    ("Algeria", "DZ", "DZA", "012"),
    ("Andorra", "AD", "AND", "020"),
    ("Angola", "AO", "AGO", "024"),
    ("Antigua and Barbuda", "AG", "ATG", "028"),
    ("Argentina", "AR", "ARG", "032"),
    ("Armenia", "AM", "ARM", "051"),
    ("Australia", "AU", "AUS", "036"),
    ("Austria", "AT", "AUT", "040"),
    ("Azerbaijan", "AZ", "AZE", "031"),
    ("Bahamas", "BS", "BHS", "044"),
    ("Bahrain", "BH", "BHR", "048"),
    ("Bangladesh", "BD", "BGD", "050"),
    ("Barbados", "BB", "BRB", "052"),
    ("Belarus", "BY", "BLR", "112"),
    ("Belgium", "BE", "BEL", "056"),
    ("Belize", "BZ", "BLZ", "084"),
    ("Benin", "BJ", "BEN", "204"),
    ("Bhutan", "BT", "BTN", "064"),
    ("Bolivia", "BO", "BOL", "068"),
    ("Bosnia and Herzegovina", "BA", "BIH", "070"),
    ("Botswana", "BW", "BWA", "072"),
    ("Brazil", "BR", "BRA", "076"),
    ("Brunei Darussalam", "BN", "BRN", "096"),
    ("Bulgaria", "BG", "BGR", "100"),
    ("Burkina Faso", "BF", "BFA", "854"),
    ("Burundi", "BI", "BDI", "108"),
    ("Cabo Verde", "CV", "CPV", "132"),
    ("Cambodia", "KH", "KHM", "116"),
    ("Cameroon", "CM", "CMR", "120"),
    ("Canada", "CA", "CAN", "124"),
    ("Central African Republic", "CF", "CAF", "140"),
    ("Chad", "TD", "TCD", "148"),
    ("Chile", "CL", "CHL", "152"),
    ("China", "CN", "CHN", "156"),
    ("Colombia", "CO", "COL", "170"),
    ("Comoros", "KM", "COM", "174"),
    ("Congo", "CG", "COG", "178"),
    ("Congo, Democratic Republic of the", "CD", "COD", "180"),
    ("Costa Rica", "CR", "CRI", "188"),
    ("Côte d'Ivoire", "CI", "CIV", "384"),
    ("Croatia", "HR", "HRV", "191"),
    ("Cuba", "CU", "CUB", "192"),
    ("Cyprus", "CY", "CYP", "196"),
    ("Czech Republic", "CZ", "CZE", "203"),
    ("Denmark", "DK", "DNK", "208"),
    ("Djibouti", "DJ", "DJI", "262"),
    ("Dominica", "DM", "DMA", "212"),
    ("Dominican Republic", "DO", "DOM", "214"),
    ("Ecuador", "EC", "ECU", "218"),
    ("Egypt", "EG", "EGY", "818"),
    ("El Salvador", "SV", "SLV", "222"),
    ("Equatorial Guinea", "GQ", "GNQ", "226"),
    ("Eritrea", "ER", "ERI", "232"),
    ("Estonia", "EE", "EST", "233"),
    ("Eswatini", "SZ", "SWZ", "748"),
    ("Ethiopia", "ET", "ETH", "231"),
    ("Fiji", "FJ", "FJI", "242"),
    ("Finland", "FI", "FIN", "246"),
    ("France", "FR", "FRA", "250"),
    ("Gabon", "GA", "GAB", "266"),
    ("Gambia", "GM", "GMB", "270"),
    ("Georgia", "GE", "GEO", "268"),
    ("Germany", "DE", "DEU", "276"),
    ("Ghana", "GH", "GHA", "288"),
    ("Greece", "GR", "GRC", "300"),
    ("Grenada", "GD", "GRD", "308"),
    ("Guatemala", "GT", "GTM", "320"),
    ("Guinea", "GN", "GIN", "324"),
    ("Guinea-Bissau", "GW", "GNB", "624"),
    ("Guyana", "GY", "GUY", "328"),
    ("Haiti", "HT", "HTI", "332"),
    ("Honduras", "HN", "HND", "340"),
    ("Hungary", "HU", "HUN", "348"),
    ("Iceland", "IS", "ISL", "352"),
    ("India", "IN", "IND", "356"),
    ("Indonesia", "ID", "IDN", "360"),
    ("Iran", "IR", "IRN", "364"),
    ("Iraq", "IQ", "IRQ", "368"),
    ("Ireland", "IE", "IRL", "372"),
    ("Israel", "IL", "ISR", "376"),
    ("Italy", "IT", "ITA", "380"),
    ("Jamaica", "JM", "JAM", "388"),
    ("Japan", "JP", "JPN", "392"),
    ("Jordan", "JO", "JOR", "400"),
    ("Kazakhstan", "KZ", "KAZ", "398"),
    ("Kenya", "KE", "KEN", "404"),
    ("Kiribati", "KI", "KIR", "296"),
    ("Korea, Democratic People's Republic of", "KP", "PRK", "408"),
    ("Korea, Republic of", "KR", "KOR", "410"),
    ("Kuwait", "KW", "KWT", "414"),
    ("Kyrgyzstan", "KG", "KGZ", "417"),
    ("Lao People's Democratic Republic", "LA", "LAO", "418"),
    ("Latvia", "LV", "LVA", "428"),
    ("Lebanon", "LB", "LBN", "422"),
    ("Lesotho", "LS", "LSO", "426"),
    ("Liberia", "LR", "LBR", "430"),
    ("Libya", "LY", "LBY", "434"),
    ("Liechtenstein", "LI", "LIE", "438"),
    ("Lithuania", "LT", "LTU", "440"),
    ("Luxembourg", "LU", "LUX", "442"),
    ("Madagascar", "MG", "MDG", "450"),
    ("Malawi", "MW", "MWI", "454"),
    ("Malaysia", "MY", "MYS", "458"),
    ("Maldives", "MV", "MDV", "462"),
    ("Mali", "ML", "MLI", "466"),
    ("Malta", "MT", "MLT", "470"),
    ("Marshall Islands", "MH", "MHL", "584"),
    ("Mauritania", "MR", "MRT", "478"),
    ("Mauritius", "MU", "MUS", "480"),
    ("Mexico", "MX", "MEX", "484"),
    ("Micronesia (Federated States of)", "FM", "FSM", "583"),
    ("Moldova (Republic of)", "MD", "MDA", "498"),
    ("Monaco", "MC", "MCO", "492"),
    ("Mongolia", "MN", "MNG", "496"),
    ("Montenegro", "ME", "MNE", "499"),
    ("Morocco", "MA", "MAR", "504"),
    ("Mozambique", "MZ", "MOZ", "508"),
    ("Myanmar", "MM", "MMR", "104"),
    ("Namibia", "NA", "NAM", "516"),
    ("Nauru", "NR", "NRU", "520"),
    ("Nepal", "NP", "NPL", "524"),
    ("Netherlands", "NL", "NLD", "528"),
    ("New Zealand", "NZ", "NZL", "554"),
    ("Nicaragua", "NI", "NIC", "558"),
    ("Niger", "NE", "NER", "562"),
    ("Nigeria", "NG", "NGA", "566"),
    ("North Macedonia", "MK", "MKD", "807"),
    ("Norway", "NO", "NOR", "578"),
    ("Oman", "OM", "OMN", "512"),
    ("Pakistan", "PK", "PAK", "586"),
    ("Palau", "PW", "PLW", "585"),
    ("Palestine, State of", "PS", "PSE", "275"),
    ("Panama", "PA", "PAN", "591"),
    ("Papua New Guinea", "PG", "PNG", "598"),
    ("Paraguay", "PY", "PRY", "600"),
    ("Peru", "PE", "PER", "604"),
    ("Philippines", "PH", "PHL", "608"),
    ("Poland", "PL", "POL", "616"),
    ("Portugal", "PT", "PRT", "620"),
    ("Qatar", "QA", "QAT", "634"),
    ("Romania", "RO", "ROU", "642"),
    ("Russian Federation", "RU", "RUS", "643"),
    ("Rwanda", "RW", "RWA", "646"),
    ("Saint Kitts and Nevis", "KN", "KNA", "659"),
    ("Saint Lucia", "LC", "LCA", "662"),
    ("Saint Vincent and the Grenadines", "VC", "VCT", "670"),
    ("Samoa", "WS", "WSM", "882"),
    ("San Marino", "SM", "SMR", "674"),
    ("Sao Tome and Principe", "ST", "STP", "678"),
    ("Saudi Arabia", "SA", "SAU", "682"),
    ("Senegal", "SN", "SEN", "686"),
    ("Serbia", "RS", "SRB", "688"),
    ("Seychelles", "SC", "SYC", "690"),
    ("Sierra Leone", "SL", "SLE", "694"),
    ("Singapore", "SG", "SGP", "702"),
    ("Slovakia", "SK", "SVK", "703"),
    ("Slovenia", "SI", "SVN", "705"),
    ("Solomon Islands", "SB", "SLB", "090"),
    ("Somalia", "SO", "SOM", "706"),
    ("South Africa", "ZA", "ZAF", "710"),
    ("South Sudan", "SS", "SSD", "728"),
    ("Spain", "ES", "ESP", "724"),
    ("Sri Lanka", "LK", "LKA", "144"),
    ("Sudan", "SD", "SDN", "729"),
    ("Suriname", "SR", "SUR", "740"),
    ("Sweden", "SE", "SWE", "752"),
    ("Switzerland", "CH", "CHE", "756"),
    ("Syrian Arab Republic", "SY", "SYR", "760"),
    ("Tajikistan", "TJ", "TJK", "762"),
    ("Tanzania, United Republic of", "TZ", "TZA", "834"),
    ("Thailand", "TH", "THA", "764"),
    ("Timor-Leste", "TL", "TLS", "626"),
    ("Togo", "TG", "TGO", "768"),
    ("Tonga", "TO", "TON", "776"),
    ("Trinidad and Tobago", "TT", "TTO", "780"),
    ("Tunisia", "TN", "TUN", "788"),
    ("Turkey", "TR", "TUR", "792"),
    ("Turkmenistan", "TM", "TKM", "795"),
    ("Tuvalu", "TV", "TUV", "798"),
    ("Uganda", "UG", "UGA", "800"),
    ("Ukraine", "UA", "UKR", "804"),
    ("United Arab Emirates", "AE", "ARE", "784"),
    ("United Kingdom", "GB", "GBR", "826"),
    ("United States", "US", "USA", "840"),
    ("Uruguay", "UY", "URY", "858"),
    ("Uzbekistan", "UZ", "UZB", "860"),
    ("Vanuatu", "VU", "VUT", "548"),
    ("Venezuela (Bolivarian Republic of)", "VE", "VEN", "862"),
    ("Viet Nam", "VN", "VNM", "704"),
    ("Yemen", "YE", "YEM", "887"),
    ("Zambia", "ZM", "ZMB", "894"),
    ("Zimbabwe", "ZW", "ZWE", "716"),
]


for name, alpha_2_code, alpha_3_code, numeric_code in countries_data:
    country, created = Country.objects.get_or_create(
        name=name,
        alpha_2_code=alpha_2_code,
        alpha_3_code=alpha_3_code,
        numeric_code=numeric_code,
    )
    if created:
        print(f'Added country: {country}')
    else:
        print(f'Country already exists: {country}')
