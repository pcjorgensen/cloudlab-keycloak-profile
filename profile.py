"""An example of constructing a profile with install and execute services. 

Instructions:
Wait for the profile instance to start, then click on the node in the topology
and choose the `shell` menu item. The install and execute services are handled
automatically during profile instantiation, with no manual intervention required.
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as rspec
# Import igext module
import geni.rspec.igext as ig

# Create a request object
request = portal.context.makeRequestRSpec()

# Create two nodes
node1 = request.RawPC("node1")

# Set each of the two to specifically request "m400" nodes, which in CloudLab, are ARM
node1.hardware_type = "m400"

# Request an image for this node
node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//CENTOS7-64-STD"

# Install and execute startup scripts
node1.addService(rspec.Execute(shell="sh", command="sudo -u root /local/repository/keycloak.sh"))

portal.context.printRequestRSpec()