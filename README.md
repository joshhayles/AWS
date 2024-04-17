# Welcome to the AWS EC2 Instance Launch with Load Balancer
This project will deploy two EC2 instances in AWS and put them behind a Load Balancer to demonstrate the ability of the Load Balancer (ALB) to "divvy" incoming traffic to multiple instances.

# Objective
- Create multiple EC2 instances in AWS (2, in this case)
- Add standard network settings for traffic:
  - use security group for inbound/outbound rules
    - Security groups are essentially firewalls for your instances, controlling inbound/outbound traffic at the instance level. You can also control the security configurations / requirements for each instance individually. They can also be applied to Load Balancers, which we'll see during this project
- Use a Python script attached to each instance that will automatically deploy a "Hello World" visual when the instance is visited via the URL
- Create Application Load Balancer to divide up instance traffic
  - create a new security group for this Load Balancer
  - add Inbound rule that allows all HTTP (port 80) from "Anywhere-IPv4"
  - allow All Traffic in Outbound rule
  - after the new SG is created, go back to the Load Balancer page (where you're creating the Load Balancer) choose the newly created security group and remove all others
  - inside 'Listeners and Routing' we need to route the traffic from port 80 to a target group. A target group is simply a group of your EC2 instances
  - create a new target group
    - after that's created, you'll be taken to the Instances screen. Choose all of those instances and click 'Include as pending' button. 
    - then click 'Create target group' button
    - back on the Load Balancer page, choose the newly created Target group
    - finish by clicking the 'Create load balancer' button at the bottom

# View Result
- You should be able to view the Hello World here (will not be kept live for long, due to costs):

LB-EC2-Hello-World-1259031245.us-east-1.elb.amazonaws.com

# Result (screenshots)
![Place where Python script is pasted in the EC2 instance (in the User Data section)](image.png)