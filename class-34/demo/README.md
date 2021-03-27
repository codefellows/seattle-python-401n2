# Steps for Deployment

- Make sure your .env is setup and installed.
- Update your settings.py to ensure that all required items are reading from your .env
- Do not forget your .gitignore
- Update CORS, WHITENOISE in project
- Connectt o external database (if you want to)
- Research online deployemnt methods and pick a host to deploy to.

## Helpful Resources

[A Quick Reference](https://stackabuse.com/deploying-django-applications-to-aws-ec2-with-docker/)
[Reference 2](https://testdriven.io/blog/django-docker-https-aws/)
[Reference 3](https://try.digitalocean.com/deploy-django/?utm_campaign=amer_app_platform_kw_en_cpc&utm_adgroup=deploy_django&_keyword=%2Bdjango%20%2Bdeploy&_device=c&_adposition=&utm_content=conversion&utm_medium=cpc&utm_source=google&gclid=CjwKCAjwr_uCBhAFEiwAX8YJgXskoOQkDmIscZOYjfdztw60P2h2mynnRyRPbIgl2mNmAtvNsDU1QRoCCt8QAvD_BwE)
[Reference 4](https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9)
[Reference 5](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html)
[Heroku](https://devcenter.heroku.com/categories/deploying-with-docker)

## SSH - AWS
- copy .pem file to .ssh folder
- chmod 400 file.pem
- ssh -i file.pem ec2-user@YOurPublicDNS.compute.amazonaws.com

# EC2
- Set incomming permissions for port 8000

## EC2 Instance
- Install updates
- Install git
- Install Docker
- Install Docker Compose
- Clone Repo