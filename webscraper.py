import os

# each website will create a new dir

def create_project_dir(directory):
	if not os.path.exists(directory):
		print(f'Creating directory {directory}')
		os.makedirs(directory)
	else:
		print ('that directory already exists')

create_project_dir('robertest')