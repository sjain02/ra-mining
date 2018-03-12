import os
class RAUtilities:
    def FileHandle(self, directory, filename, overwrite):
        os.chdir(directory)
        if (os.path.exists(filename)==True and overwrite==False):
            # 2 syntax
            #fp= open(filename,'ab')
            # 3 syntax
            fp= open(filename,'a')
        else:
            #fp= open(filename, 'wb')
            fp= open(filename, 'w')
        return fp
    def sortFileIndex(self,fNameA,fNameB):
        s1=s2=[]
        s1=fNameA.rsplit('.')
        s2=fNameB.rsplit('.')
        if len(s1) == len(s2)==3:
            if(int(s1[2])<int(s2[2])):
                return -1
            elif (int(s1[2])>int(s2[2])):
                return 1
