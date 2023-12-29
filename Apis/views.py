from rest_framework.views import APIView
from django.http import HttpResponse
import requests
import json
from Account import manager
from datetime import datetime
from Apis.models import AppInfo, Report
import urllib.request
import re
import yt_dlp
# Create your views here.

class Download(APIView):
    def post(self, request, formate=None):
        try:
            url_data = request.POST.get("urldata")

            if url_data:
                if "http" not in url_data:
                    title = url_data.replace("%20"," ").replace("%22","\"")
                    search_song_url = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={url_data}")
                    video_ids = re.findall(r"watch\?v=(\S{11})", search_song_url.read().decode())
                    url_data = str("https://www.youtube.com/watch?v=" + video_ids[0])
                    video_info = yt_dlp.YoutubeDL().extract_info(url_data, download = False)
                    download_link = None
                    formate = video_info.get("formats")
                    preferred_formats = ["1080p", "720p", "480p", "360p", "240p", "144p"]
                    for quality in preferred_formats:
                        new_data = list(filter(lambda d:d['format_note'] == quality if "format_note" in d else "", formate))
                        for data in new_data:
                            if data["ext"] == "mp4":
                                download_link = data["url"]
                                break
                        if download_link:
                            break
                    download_link = [{"n_link_url":download_link,'n_link_title':title,'n_link_extension':"mp4",'n_link_quality':quality}]
                    return HttpResponse(json.dumps({"links_data":download_link, "status": 1, "message": "Download information"}))
                elif "https://yout" in url_data or "https://www.youtube" in url_data:
                    if "?v" in url_data or "?si" in url_data or "shorts" in url_data:
                        if "&list" in url_data:
                            url_data= url_data.split("&list")[0]
                        video_info = yt_dlp.YoutubeDL().extract_info(url_data, download = False)
                        title = video_info.get("title")
                        download_link = None
                        formate = video_info.get("formats")
                        preferred_formats = ["720p", "480p", "360p", "240p", "144p"]
                        for quality in preferred_formats:
                            new_data = list(filter(lambda d:d['format_note'] == quality if "format_note" in d else "", formate))
                            for data in new_data:
                                if data["ext"] == "mp4":
                                    download_link = data["url"]
                                    break
                            if download_link:
                                break
                        download_link = [{"n_link_url":download_link,'n_link_title':title,'n_link_extension':"mp4",'n_link_quality':quality}]
                        return HttpResponse(json.dumps({"links_data":download_link, "status": 1, "message": "Download information"}))
                    else:
                        return HttpResponse(json.dumps({"links_data":"", "status": 0, "message": "Video not found"}))
                else:
                    url = "https://guidapis.xyz/bxdown/home/meddata"
                    payload = {"vercode":4.2 , "urldata":url_data}
                    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                    response = requests.request("POST", url, headers=headers, data=payload).json()
                    if "links_data" in response:
                        response = response["links_data"]
                        return HttpResponse(json.dumps({"links_data":response, "status": 1, "message": "Download information"}))
                    else:
                        return HttpResponse(json.dumps({"links_data":"", "status": 0, "message": "Video not found"}))
            else:
                return HttpResponse(json.dumps({"links_data":"", "status": 0, "message": "Video not found"}))
        except Exception as e:
            manager.create_from_exception(e)
            return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(e)}))


class AppInfoView(APIView):
    def get(self, request, formate=None):
        try:
            device_id =  request.POST.get("device_id")
            device_name = request.POST.get("type")
            device_name = AppInfo.objects.get(device = device_name)
            report, created = Report.objects.get_or_create(device_id=device_id, device_name=device_name, defaults={'first_login_date': datetime.now(),'last_login_date': datetime.now()})
            if not created:
                report.last_login_date= datetime.now()
                report.save()
            queryset = AppInfo.objects.all().values()
            main ={}
            for i in queryset:
                dic1 = {}
                dic1["version"]=i["version"]
                dic1["url"]=i["url"]
                dic1["force_update"]=i["force_update"]
                main[i["device"]]=dic1
            return HttpResponse(json.dumps({"data":main, "status": 1, "message": "App information"}))
        except Exception as e:
            manager.create_from_exception(e)
            return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(e)}))



# class Download(APIView):
#     def post(self, request, formate=None):
#         try:
#             url_data = request.POST.get("urldata")
#             print(url_data)
#             if url_data:
#                 if "http" not in url_data:
#                     search_song_url = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={url_data}")
#                     video_ids = re.findall(r"watch\?v=(\S{11})", search_song_url.read().decode())
#                     url_data = str("https://www.youtube.com/watch?v=" + video_ids[0])
#                 # headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#                 # data = {"vercode":4.2,"urldata":url_data}
#                 # response = requests.request("POST","https://guidapis.xyz/bxdown/home/meddata", headers=headers, data=data).json()
#                 search_song_url = urllib.request.urlopen("https://www.youtube.com/watch?v=iqLyIMoEDQM")
#                 print(urllib.parse.urlparse("https://www.youtube.com/watch?v=iqLyIMoEDQM"))
#                 file_info=search_song_url.read()
#                 file_info_str=str(file_info)
#                 file_lines=file_info_str.split('\\n')
#                 newfile=open('file.txt','w')
#                 for info in file_lines:
#                     newfile.write(info +'\n')
#                 newfile.close()
#                 # print(video_ids)
#                 # response = requests.request("GET","https://bhm.progmore.com/blackhole.php?url=https://www.youtube.com/watch?v=BA3GMVDChUw")
#                 # print(response.json())
#                 # print(response.text)
#                 response = response
#             return HttpResponse(json.dumps({"links_data":response, "status": 1, "message": "Download information"}))
#         except Exception as e:
#             manager.create_from_exception(e)
#             return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(e)}))





# class Download(APIView):
#     def post(self, request, formate=None):
#         try:
#             url_data = request.POST.get("urldata")
#             title = url_data
#             if url_data:
#                 if "http" not in url_data:
#                     search_song_url = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={url_data}")
#                     video_ids = re.findall(r"watch\?v=(\S{11})", search_song_url.read().decode())
#                     url_data = str("https://www.youtube.com/watch?v=" + video_ids[0])
#                 video_info = yt_dlp.YoutubeDL().extract_info(url_data, download = False)
#                 download_link = None
#                 formate = video_info.get("formats")
#                 preferred_formats = ["2160p", "1440p", "1080p", "720p", "480p", "360p", "240p", "144p"]
#                 for quality in preferred_formats:
#                     new_data = list(filter(lambda d:d['format_note'] == quality if "format_note" in d else "", formate))
#                     for data in new_data:
#                         if data["ext"] == "mp4":
#                             download_link = data["url"]
#                             break
#                     if download_link:
#                         break
#                 download_link = [{"n_link_url":download_link,'n_link_title':title,'n_link_extension':"mp4",'n_link_quality':quality}]
#             return HttpResponse(json.dumps({"links_data":download_link, "status": 1, "message": "Download information"}))
#         except Exception as e:
#             manager.create_from_exception(e)
#             return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(e)}))