from bioblend import galaxy

# GalaxyInstance
gi = galaxy.GalaxyInstance(url='http://127.0.0.1:8080', key='05e209eb9960db20f5b85a132304cc7a')
hl = gi.histories.get_histories()

# Config
# Contains possible interaction dealing with Galaxy configuration.
conf = galaxy.config.ConfigClient(gi)
conf.get_config()
conf.get_version()

# Datasets
# Contains possible interactions with the Galaxy Datasets
dataset = galaxy.datasets.DatasetClient(gi)
dataset.download_dataset()
dataset.show_dataset()
dataset.show_stderr()
dataset.show_stdout()

# Datatypes
# Contains possible interactions with the Galaxy Datatype
datatype = galaxy.datatypes.DatatypesClient(gi)
datatype.get_datatypes()
datatype.get_sniffers()

# Folders
# Contains possible interactions with the Galaxy library folders
folders = galaxy.folders.FoldersClient(gi)
folders.create_folder()
folders.delete_folder()
folders.get_permissions()
folders.set_permissions()
folders.show_folder()
folders.update_folder()

# Forms
# Contains possible interactions with the Galaxy Forms
forms = galaxy.forms.FormsClient(gi)
forms.create_form()
forms.get_forms()
forms.show_form()

# FTP files
# Contains possible interactions with the Galaxy FTP Files
ftp = galaxy.ftpfiles.FTPFilesClient(gi)
ftp.get_ftp_files()

# Genomes
# Contains possible interactions with the Galaxy Histories
genome = galaxy.genomes.GenomeClient(gi)
genome.get_genomes()
genome.show_genome()

# Groups
# Contains possible interactions with the Galaxy Groups
groups = galaxy.groups.GroupsClient(gi)
groups.add_group_role()
groups.add_group_user()
groups.create_group()
groups.delete_group_role()
groups.delete_group_user()
groups.get_group_roles()
groups.get_group_users()
groups.get_groups()
groups.show_group()
groups.update_group()

# Histories
# Contains possible interactions with the Galaxy Histories
history = galaxy.histories.HistoryClient(gi)
history.create_dataset_collection()
history.create_history()
history.create_history_tag()
history.delete_dataset()
history.delete_dataset_collection()
history.delete_history()
history.download_dataset()
history.download_history()
history.export_history()
history.get_current_history()
history.get_histories()
history.get_most_recently_used_history()
history.get_status()
history.show_dataset()
history.show_dataset_collection()
history.show_dataset_provenance()
history.show_history()
history.show_matching_datasets()
history.undelete_history()
history.update_dataset()
history.update_dataset_collection()
history.update_history()
history.upload_dataset_from_library()


# Jobs
# Contains possible interactions with the Galaxy Jobs
jobs =  galaxy.jobs.JobsClient(gi)
jobs.get_jobs()
jobs.get_state()
jobs.search_jobs()
jobs.show_job()

# Libraries
# Contains possible interactions with the Galaxy Data Libraries
libraries = galaxy.libraries.LibraryClient(gi)
libraries.copy_from_dataset()
libraries.create_folder()
libraries.create_library()
libraries.delete_library()
libraries.delete_library_dataset()
libraries.get_folders()
libraries.get_libraries()
libraries.get_library_permissions()
libraries.set_library_permissions()
libraries.show_dataset()
libraries.show_folder()
libraries.show_library()
libraries.upload_file_contents()
libraries.upload_file_from_local_path()
libraries.upload_file_from_server()
libraries.upload_file_from_url()
libraries.upload_from_galaxy_filesystem()

# Quotas
# Contains possible interactions with the Galaxy Quota
quotas = galaxy.quotas.QuotaClient(gi)
quotas.create_quota()
quotas.delete_quota()
quotas.get_quotas()
quotas.show_quota()
quotas.undelete_quota()
quotas.update_quota()

# Roles
# Contains possible interactions with the Galaxy Roles
roles = galaxy.roles.RolesClient(gi)
roles.create_role()
roles.get_roles()
roles.show_role()

# Tools
# Contains possible interaction dealing with Galaxy tools.
tools = galaxy.tools.ToolClient(gi)
tools.get_tool_panel()
tools.get_tools()
tools.install_dependencies()
tools.paste_content()
tools.put_url()
tools.run_tool()
tools.show_tool()
tools.upload_file()
tools.upload_from_ftp()

# Tool data tables
# Contains possible interactions with the Galaxy Tool data tables
tool_data = galaxy.tool_data.ToolDataClient(gi)
tool_data.delete_data_table()
tool_data.get_data_tables()
tool_data.reload_data_table()
tool_data.show_data_table()


# ToolShed
# Interaction with a Galaxy Tool Shed.
toolshed = galaxy.toolshed.ToolShedClient(gi)
toolshed.get_repositories()
toolshed.install_repository_revision()
toolshed.show_repository()

# Users
# Contains possible interaction dealing with Galaxy users.
users = galaxy.users.UserClient(gi)
users.create_local_user()
users.create_remote_user()
users.create_user_apikey()
users.delete_user()
users.get_current_user()
users.get_user_apikey()
users.get_users()
users.show_user()

# Visual
# Contains possible interactions with the Galaxy visualization
visual = galaxy.visual.VisualClient(gi)
visual.get_visualizations()
visual.show_visualization()

# Workflows
# Contains possible interactions with the Galaxy Workflows
workflows = galaxy.workflows.WorkflowClient(gi)
workflows.cancel_invocation()
workflows.delete_workflow()
workflows.export_workflow_dict()
workflows.export_workflow_json()
workflows.export_workflow_to_local_path()
workflows.get_invocations()
workflows.get_workflow_inputs()
workflows.get_workflows()
workflows.import_shared_workflow()
workflows.import_workflow_dict()
workflows.import_workflow_from_local_path()
workflows.import_workflow_json()
workflows.invoke_workflow()
workflows.run_invocation_step_action()
workflows.run_workflow()
workflows.show_invocation()
workflows.show_invocation_step()
workflows.show_workflow()
