import sys, getopt
import logging
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.ERROR)
from infoblox_client import connector
from infoblox_client import objects
#from IPy import IP

def a2ptr(ip,username,password,dnsview,dns_auth_zone,ssl_verify):

   opts = {'host': ip, 'username': username, 'password': password, 'ssl_verify': ssl_verify}
   conn = connector.Connector(opts)
   records = conn.get_object('record:a', {"view":dnsview, 'zone':dns_auth_zone})


   for record in records:
       print "name: " + record["name"] +" = IP: " + record["ipv4addr"]
       ptr = record["ipv4addr"]
       print "adding: " + record["ipv4addr"] + " to ARPA Zone: " + IP(record["ipv4addr"]).reverseName()[:-1] + " with Name: " + record["name"]
       ##print "ARPA Correct Format: ", IP(record["ipv4addr"]).reverseName()[:-1]
       objects.PtrRecord.create(conn, view='default', ptrdname=record["name"], ipv4addr=ptr)

   #print 'Number of arguments:', len(sys.argv), 'arguments.'
   #print 'Argument List:', str(sys.argv)



def main(argv):
   ip = ''
   username = ''
   password = ''
   dnsview = ''
   dns_auth_zone = ''
   ssl_verify = 'false'

   try:
      opts, args = getopt.getopt(argv,"hi:u:p:v:z:",["xxxx=","yyyy="])
#      print opts
#     print args
   except getopt.GetoptError:
      print 'infoblox_generate_ptr_from_a_records.py -i <Infoblox_IP> -u <username> -p <password> -v <dnsview> -z <DNSZone>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'infoblox_generate_ptr_from_a_records.py -i <Infoblox_IP> -u <username> -p <password> -v <dnsview> -z <DNSZone>'
         sys.exit()
      elif opt in ("-i", "--ip"):
         ip = arg
      elif opt in ("-u", "--username"):
         username = arg
      elif opt in ("-p", "--password"):
         password = arg
      elif opt in ("-v", "--dnsview"):
         dnsview = arg
      elif opt in ("-z", "--DNSZone"):
         dns_auth_zone = arg

   a2ptr(ip, username, password, dnsview, dns_auth_zone, ssl_verify)
   print '**************************************'
   print 'Infoblox IP is:', ip
   print 'dnsview is:', dnsview
   print 'DNS Zone is:', dns_auth_zone
   print '**************************************'
if __name__ == "__main__":
   main(sys.argv[1:])

#a2ptr(host,username,password,view,dns_auth_zone,ssl_verify)
