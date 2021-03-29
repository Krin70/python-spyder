from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = "https://www.zhihu.com/people/edit"
headers = {
    "User-Agent": UserAgent().chrome,
    "Cookie": '''_zap=36a4c405-66cb-4162-bcfe-2ac4af1b03ba; d_c0="ADBXWK8FZhKPTvhur9UYkNRm7hnp2513v2s=|1608864239"; r_cap_id="NjA5MDg1YTE5NjRiNGYzYTkzYWI0OGQ3MDhjMTg0ZjE=|1609577500|8d09fbb4915fe680abcce09a03bfc8a00e3eb677"; cap_id="NGJjYTI1YWIzZmM0NDY1Nzg2MGM4NjU5NjZkZmNiOGI=|1609577500|def1db830671d176546fa1fd008300f8e4f78081"; l_cap_id=\"NDcyZWMyNjdlZmQwNDk3Mjk5MmUzYjZhODI1NjgxZGI=|1609577501|72d10a8f519c949bc2eafbc8bffc97a8aec48281"; capsion_ticket="2|1:0|10:1609577524|14:capsion_ticket|44:NjljZmU2YmQ3N2E5NDkwNjgwZmI1YjkyYjgyYzlmZDU=|263356138c4c1452771f0481afffc87220548ed7e702db59c322d0459bafc078"; auth_type=cXFjb25u|1609577618|2f7746eda4f83dcd4c1dd17d2fbd77492ad5c460; token="NTI2QTcyRTM5Qzg5QjQ3OTI3NzYxMDVCMTY5NTk4NTA=|1609577618|870f9b916685aacebf71942fa17e316fa2ffe818"; client_id="MTBGMUE2MUVCOTA3RTk4QUI3RDkwRTg0NkRERjY3REI=|1609577618|3b3db0e1c2c188020cecb2285ffe98db9559079f"; z_c0=Mi4xNUlwY0JRQUFBQUFBTUZkWXJ3Vm1FaGNBQUFCaEFsVk4zWUxkWUFBbTBOSEFaSms3aUlCcktHMUxLSnU3VWkybmRB|1609577693|ce1ef503c6e592d590c0ca23173b5dc17d4b2b46; tst=r; q_c1=5caa908792eb4f40bb7dafc9243fc00b|1609659033000|1609659033000; ISSW=1; _xsrf=bb232dbd-7d0f-463d-9467-88ee1334258e; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1611632512,1611650361,1611650636,1611650998; SESSIONID=v79tdbUGFxf43DzYOmeJoGuSrbCS931hzfmybRDCgfb; JOID=Vl8SBU-vgwIFJQ-XbK3wGEMVlf592rQ6c0Fuwirp-GQwFEvuNe6BEWcmDJZvaFOsjOENBvSJFW50KGZEq1yr-jo=; osd=UVgXC06ohAcLJAiQaaPxH0QQm_963bE0ckZpxyTo_2M1GkrpMuuPEGAhCZhub1SpguAKAfGHFGlzLWhFrFuu9Ds=; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1611662282|1611662141; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1611662282'''
}
request = Request(url, headers=headers)
response = urlopen(request)

print(response.read().decode())
