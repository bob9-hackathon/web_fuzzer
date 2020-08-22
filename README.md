### bob web-fuzzer
<hr>

### introduction

```bash
1. Team Leader. 박찬솔
2. Team Member(1) 안평주
3. Team Member(2) 석지원
4. Team Member(3) 장재원
5. Team Member(4) 정상훈
6. Team Member(5) 정동현
```

### Requirements
`pip3 install selenium requests`

### Execute
#### XSS
`python.exe .\main.py -urls "http://127.0.0.1/xss_get" -seed .\seed\xss\xss.txt -params "xss=@"`
> Web Server : [XSS_Server](https://github.com/bob9-hackathon/XSS_Server)