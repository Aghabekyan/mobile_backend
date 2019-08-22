docker build -t aghabekyan374/mobile-backend:latest -t aghabekyan374/mobile-backend:$SHA -f ./Dockerfile .

docker push aghabekyan374/mobile-backend:latest

docker push aghabekyan374/mobile-backend:$SHA
