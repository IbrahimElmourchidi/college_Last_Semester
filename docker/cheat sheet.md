# Docker Commands Cheat Sheet

**001 : To run an Image:**

<code>
    
    docker run image-name

    // running an image is basically two commands:
    
        1. docker create image_name 
        // this will create a container from the image
        
        2. docker start -a container_id 
        // this will execute the default start up command
    # docker run  = docker create + docker start
</code>
<hr>

**002 : To run an Image and override the default command:**

<code>

    docker run image-name command

</code>
<hr>

**003 : To List All currently running images:**

<code>
    
    docker ps

</code>
<hr>

**004 : To list all images that was ever ran on his machine**

<code>
    
    docker ps --all

</code>
<hr>

**005 : To start a docker container**

<code>
    
    docker start -a container_id

    note: -a is used to print the output

</code>
<hr>


**006 : To create a docker container**

<code>
    
    docker create image_name

    // this command will print the id of the container created
</code>
<hr>

**007 : To Delete All Images**

<code>
    
    docker system prune

    // this command will delete all stopped container as well as the build cache
</code>
<hr>

**008 : To get all the emitted output from a container**

<code>
    
    docker logs contanier_id

</code>
<hr>

**009 : To stop a container**

<code>
    
    // send a terminate signal to the container
    docker stop contanier_id

    // brutly stop the container using a kill signal
    docker kill container_id 
</code>
<hr>

**010 : To execute command in the running container**

<code>
    
    docker exec -it container-id command
</code>
<hr>

**011 : To run terminal on the container**

<code>
    
    docker exec -it container-id sh
</code>
<hr>

