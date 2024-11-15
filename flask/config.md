### [config.md]("file:///c:/Users/Slmss/OneDrive/Desktop/Data-Science-Dummy-main/flask/config.md")



# Deployment Instructions

## Step 1: Configure AWS EKS
Follow the instructions in the [AWS EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html) to create your kubeconfig file.

Run the following command to update your kubeconfig:
```sh
aws eks --region ap-south-1 update-kubeconfig --name slm
```

## Step 2: Build Docker Image
Build the Docker image for your Flask application:
```sh
docker build --platform linux/amd64 -t flask/app .
```

## Step 3: Push Docker Image to ECR
Tag and push your Docker image to Amazon ECR:
```sh
# Tag the image
docker tag flask/app:latest 043309325682.dkr.ecr.us-east-1.amazonaws.com/flask/app:latest

# Push the image
docker push 043309325682.dkr.ecr.us-east-1.amazonaws.com/flask/app:latest
```

## Step 4: Deploy to Kubernetes
Apply the Kubernetes deployment and service configuration:
```sh
kubectl apply -f deployment.yaml
```

## Step 5: Verify Deployment
Check the status of your pods to ensure they are running correctly:
```sh
kubectl get pods -n slmsshk
```

Check the logs of a specific pod if needed:
```sh
kubectl logs <pod-name> -n slmsshk
```

## Step 6: Access the Application
Once the service is up and running, you can access your Flask application using the external IP provided by the LoadBalancer service. Run the following command to get the external IP:
```sh
kubectl get svc -n slmsshk
```

Look for the `service` column in the output.

run
```
kubectl port-forward svc/flask-app-service 8080:80
```
head to: `http://localhost:8080`

# Thank you
