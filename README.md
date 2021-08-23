This is a template project I use to build a **simple** and **free** cloud hosted application.

The focus is **free**. Too often I build a web application that costs a small but annoying amount of money every month. Inevitably, I end up shutting it down, after paying for the service for a couple years.

I decided to go ahead and build a stack that can be hosting in the cloud for free forever, assuming the usage stays under some amount.

The stack for this template is:

### Stack
Every part of this stack is free for apps that have low usage.

**Frontend**
* Bootstrap
* JQuery
* AlpineJS

**Backend**
* FastAPI

**Secrets Management**
* dot-env

**Storage**
* DynamoDB (storage of 25GB, free forever)
* Imgur (image storage, free forever)

**Infrastructure**
* Docker Container
* Google Cloud Run (50 hours of vCPU seconds, free forever) *

\* *50 hours = 180,000 seconds. If your average response time is 1 second, and your app can run on a 512 GHz CPU, Google Cloud Run will host approximately 180,000 requests. See full details [here](https://cloud.google.com/run/pricing)*

### Installation
```
git clone https://github.com/czhu12/free-cloud-app-template

cd free-cloud-app-template

./bin/install

# Update .env file with proper credentials

./bin/deploy
```
