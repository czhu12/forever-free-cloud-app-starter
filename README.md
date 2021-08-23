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
git clone https://github.com/czhu12/forever-free-cloud-app-starter

cd forever-free-cloud-app-starter

./bin/install

# Update .env file with proper credentials

./bin/deploy
```

### What's next?
In my experience building small DB backed applications, having a nice high-level, black-box functional testing environment is really nice. All I want to know is that a syntax error won't cause the whole app to fail to boot, or the main feature of the app is completely broken. I think the right way to do this is a Docker environment that:
1. Installs the application
2. Mocks out DynamoDB
3. Run's pytest against a known port.
