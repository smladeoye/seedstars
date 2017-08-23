import jenkins
from datetime import datetime
from seedstars.models import Jobs

class jenkinsApi:

    connection = None

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def connect(self):
        if (self.connection == None):
            self.connection = jenkins.Jenkins(self.url, self.username, self.password)
        return self.connection

    def getJobs(self):
        connection = self.connect()
        return connection.get_jobs()

    def getJobInfo(self, name):
        connection = self.connect()
        return connection.get_job_info(name)

    def getJobBuildInfo(self,name,number):
        return self.connect().get_build_info(name,number)


    def saveBuildInfo(self):
        # Uses the connection to get jobs build information and saves to the jobs table

        jobs = self.getJobs()

        if (jobs is not None):
            for value in jobs:
                job_name = value['name']
                job_info = self.getJobInfo(job_name)
                first_build = job_info['firstBuild']
                if (first_build != None):
                    all_builds = job_info['builds']
                    for build in all_builds:
                        build_number = build['number']
                        print(build)
                        build_info = self.getJobBuildInfo(job_name, build_number)
                        status = build_info['result']
                        time = datetime.now()
                        print(build_info)
                        job = Jobs(name=job_name, build_number=build_number, status=status, checked_time=time)
                        job.save()