# bot 생성을 위한 설정
```
hermes profile list
hermes gateway status
hermes config set gateway.multiplex_profiles true
hermes gateway restart
hermes gateway run
```

# 각 profile 상태 확인
```
hermes profile list
hermes -p careermate-supervisor gateway status
hermes -p fit-agent gateway status
hermes -p strategy-agent gateway status
```