#! /bin/sh

## remove BPDB_Project directory
echo "\n  ----> removing REMOTE awsdemo directory "
ssh -i ~/coleidab_django.pem  ubuntu@18.144.84.251 "rm -rf  ~/django_projects/awsdemo"
## create BPDB_Project directory
echo "\n  ----> creating REMOTE awsdemo directory "
ssh -i ~/coleidab_django.pem  ubuntu@18.144.84.251  "mkdir -p ~/django_projects/awsdemo"
## copy BPDB source files
echo
echo  "  ----> copy DJANGO PROJECTS files to Web Server  "
echo
scp -r -i ~/coleidab_django.pem acmeparts/ \
                                acmeparts/ \
                                manage.py \
                                static/ \
                                collectstatic/ \
                                requirements.txt \
                                ubuntu@18.144.84.251:~/django_projects/acmeparts


# create virtual environment
# echo "\n  ----> Create Virtual Development Env called vdev and Activate "
# ssh -i ~/bpdb-app.pem  ubuntu@10.148.72.91 "python3 -m venv vdev"
# ssh -i ~/bpdb-app.pem  ubuntu@10.148.72.91 "sudo source vdev/bin/activate"
# ssh -i ~/bpdb-app.pem  ubuntu@10.148.72.91 "sudo vdev/bin/activate"
# install project requirements
# echo "\n  ----> Install Project Requirements "
# ssh -i ~/bpdb-app.pem  ubuntu@10.148.72.91 "pip install -r requirements.txt"

# echo "\n  ----> List vdev AWSDEMO installed Requirements "
# ssh -i ~/bpdb-app.pem  ubuntu@10.148.72.91 "pip list"

## create BPDB_Project directory
echo "\n  ----> directory listing "
ssh -i ~/coleidab_django.pem  ubuntu@18.144.84.251  "tree -L 2 ~/django_projects/acmeparts"
ssh -i ~/coleidab_django.pem  ubuntu@18.144.84.251  "tree ~/django_projects/acmeparts" > files_copied_to_host.txt

# end of process
echo
echo  "  ----> completed copying SOURCE to DJANGO project web server "


