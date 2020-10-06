# -*- coding: utf-8 -*-
from django.views import View
import django_rq
from django.http import JsonResponse
from django.http import HttpResponse
import json
import datetime
from Jobs.testjob import test
'''
it is a template project to put django&rq&vue-template together.
* django provide backend management.
* django-rq provide asyn job(managed by django).
* vue-template provide frontend template which contains permission manage,axios,element-ui.
it will help you to build up a project quickly which  contains frontend&backend&job scheduling.
by pony@lixiang
'''

class JobStatus(View):
    '''
    check the status of the Jobs.
    '''
    def get(self, request):
        queue = django_rq.get_queue('low') #get the task queue 'low'.
        rq_id = "job_test_id1" # get the job id(may be from database.)
        rq_job = queue.fetch_job(rq_id)
        if rq_job:
            if rq_job.is_finished: #julge if the task is finished.
                data={
                    "status":"200",
                    "data":u"job finished.",
                    "time":str(datetime.datetime.now())[:19]
                }
                return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')

            elif rq_job.is_failed: #julge if the task is failed.
                rq_job.delete() #delete the job.
                data={
                    "status":"200",
                    "data":u"job failed.",
                    "time":str(datetime.datetime.now())[:19]
                }
                return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')
            else:#is still running.
                data={
                    "status":"200",
                    "data":u"still running.",
                    "time":str(datetime.datetime.now())[:19]
                }
                return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')

class PushJob(View):
    '''
    push the job into the queue.
    '''
    def get(self, request):
        queue = django_rq.get_queue('low') #get the queue 'low'.
        rq_id = "job_test_id1" # set the job id(save to database).
        queue.enqueue_call(
	        func=test,
	        args=(),
	        timeout=3600,
	        job_id=rq_id,
	    )
        data = {
            "status": "200",
            "data": rq_id,
            "time": str(datetime.datetime.now())[:19]
        }
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')