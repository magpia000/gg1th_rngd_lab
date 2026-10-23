# 모델 실행하기
- furiosa-ai/Qwen3-8B-FP8 모델 서빙하기
```
furiosa-llm serve furiosa-ai/Qwen3-8B-FP8 \
  --reasoning-parser qwen3 \
  --default-chat-template-kwargs '{"enable_thinking": false}'
```

# jupyter lab 실습 환경 구성

- ipykernel 설치
```
uv add ipykernel
```

- jupyter kernel에 등록
```
uv run python -m ipykernel install --user \
    --name .venv \
    --display-name "Python (rngd-lab)"
```

# 필요한 라이브러리 설치
```
uv add langchain langchain_openai tavily
```


- vscode에서 확장프로그램 설치
![alt text](images/image.png)