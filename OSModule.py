import os
import sys

#print('cwd',os.getcwd()) #Current Working Directory
cwd = os.getcwd()


#os.chdir('/home/arjunsingh/Desktop') # Changing directory name
#print(os.listdir()) # List the folders on that path


#os.mkdir('Python-Makedit')
#os.makedirs('Python-Makedit/Boom/Boom')
#os.removedirs('Python-Makedit/Boom/Boom')

#print(os.stat('boom.txt'))


# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print('Directory Path', dirpath)
#     print('Directory Folders', dirnames)
#     print('Fle Names', filenames)

#for i in os.environ:
#    print(i, os.environ[i])


# Create a new file with path instead using str concat as it causes trouble by '/' as well as it may be os restricted so use path.join method

#file_name = 'text.txt'
#file_path = os.path.join(os.getcwd(),file_name)
#print('file path', file_path)
#with open(file_path, 'w') as f:
#    f.write('Boom')


#print('os.path', dir(os.path))


# Searching for a file in the directory and all sub-directories in it
# If no file path is given i.e. only file name is given, then it will search only in current working directory and if no file name is given then it will give error

# suppose if the second argument is the path and the third one is the filename, then checking for that too in the if condition

if __name__=='__main__':
    try:
        directory_name, file_name = sys.argv[1], sys.argv[2]
    except:
        directory_name, file_name = os.path.split(sys.argv[1])
    if file_name:
        if directory_name:
            dir_name = directory_name
        else:
            dir_name = os.getcwd()
            
        for dirpath, dirnames, filenames in os.walk(dir_name):
            for filename in filenames:
                if filename == file_name:
                    print('Found the file in {}'.format(dirpath))
                    sys.exit()
    print('Incorrect Path/FileName provided or the file is not present')
    
