from bioblend import galaxy

# GalaxyInstance
gi = galaxy.GalaxyInstance(url='http://127.0.0.1:8080', key='aa0b3519ac0b89ce5ee38989063100bf')

libraries = galaxy.libraries.LibraryClient(gi)
lib = libraries.create_library(name='test', description='test', synopsis='test')

libraries.get_library_permissions(lib['id'])

folder = libraries.create_folder(lib['id'], 'test')

folder_id = folder[0]['id']

libraries.upload_file_from_local_path(libid, '/home/xfu/Project/Rosa/RNA-Seq/fastq/test/L2_4_1_R1.fastq.gz', fid)
libraries.upload_from_galaxy_filesystem(lib['id'], '/home/xfu/Project/Rosa/RNA-Seq/fastq/test/L2_4_1_R1.fastq.gz', folder_id)

