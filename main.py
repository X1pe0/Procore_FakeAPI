import os
import sys
import time
import subprocess
import readline
company_id='123456'
txt = subprocess.check_output("""curl -s -F grant_type=client_credentials \
-F client_id=12345678910 \
-F client_secret=12345678910 \
-X POST https://login.procore.com/oauth/token
""", shell=True)
parse = txt.replace('"access_token":"','').replace('}','').replace('{','')
sep = '''","token_type":'''
strip = parse.split(sep, 1)[0]
try:
	ids = str(sys.argv[1])
	try:
		apic = str(sys.argv[2])
		if ids == 'proj':
			projid = str(sys.argv[3])
	except:
		pass
except:
	print ('''
Script.py API Help:

script.py comp <COMPANY API CALLS>
script.py proj <PROJECT API CALLS> <PROJ-ID>
                                  -----
To List Company API Calls: script.py company_command_list
To List Project API Calls: script.py project_command_list

Show Company: script.py whoami

List Projects: script.py proj_list

	''')
	exit(0)
if ids == 'company_command_list':
	print ('''
	uploads
	construction_volume/urgent_error
	programs
	project_bid_types
	project_owner_types
	project_regions
	project_stages
	project_types
	roles
	submittal_statuses
	trades
	people/inactive
	users/inactive
	vendors/inactive
	insurances
	people
	permission_templates
	users
	vendors/{vendor_id}/insurances
	file_versions
	''')
	exit(0)
if ids == 'project_command_list':
	print ('''
	configurable_field_sets
	daily_log_headers
	''')
	exit(0)
try:
	if ids == 'proj':
		main = subprocess.check_output('curl -s -H "Authorization: Bearer %s" -F company_id=%s -X GET https://api.procore.com/rest/v1.0/projects/%s/%s | python -m json.tool'%(strip,company_id,projid,apic), shell=True)
	if ids == 'comp':
		main = subprocess.check_output('curl -s -H "Authorization: Bearer %s" -X GET https://api.procore.com/rest/v1.0/companies/%s/%s | python -m json.tool'%(strip,company_id,str(apic)), shell=True)
	if ids == 'whoami':
		main = subprocess.check_output('curl -s -H "Authorization: Bearer %s" -X GET https://api.procore.com/rest/v1.0/companies/%s/ | python -m json.tool'%(strip,company_id), shell=True)
	if ids == 'proj_list':
		main = subprocess.check_output('curl -s -H "Authorization: Bearer %s" -F company_id=%s -X GET https://api.procore.com/rest/v1.0/projects/ | python -m json.tool'%(strip,company_id), shell=True)
	print (main)
except:
	pass
