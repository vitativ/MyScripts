import sys
import os

def main():
	source = 'peselv@' + sys.argv[1]
	target = sys.argv[2]
    run('scp -q %s %s' % (source,target))
	
def run(cmd):
    print cmd
    os.system(cmd)

if __name__ == '__main__':
    main()
	
#scp peselv@BuildNode:/home/peselv/workspace/Build-CourseProject/pom.xml /home/peselv
#python MyPython.py BuildNode:/home/peselv/workspace/Build-CourseProject/target/courseProject.war /home/peselv
#test
#/opt/tomcat/webapps
