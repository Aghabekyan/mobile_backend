docker build -t aghabekyan374/mobile-backend:latest -t aghabekyan374/mobile-backend:$SHA -f ./Dockerfile .

docker push aghabekyan374/mobile-backend:latest

docker push aghabekyan374/mobile-backend:$SHA

echo '12345678' | ssh corda@10.0.3.151 --password-stdin
ls
