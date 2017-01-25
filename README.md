# infoblox_gen_A2PTR
Generates PTR-Records from existing A-Records by using the Infoblox REST API


Python Module Requirement
=========================

Install infoblox-client using pip:

pip install infoblox-client


Usage:

infoblox_generate_ptr_from_a_records.py -i <Infoblox_IP> -u <username> -p <password> -v <dnsview> -z <DNSZone>
