import dnslib.server
import dnslib

class DNSLogger(dnslib.server.BaseResolver):
    def resolve(self, request, handler):
        qname = str(request.q.qname).rstrip('.')
        print(f"Received DNS request for: {qname}")

        if qname.startswith("sg") and qname.endswith(".trusted.msntv.msn.com"):
            try:
                # Extract the part between 'sg' and '.trusted.msntv.msn.com'
                parts = qname.split('.')
                if len(parts) < 3:
                    raise ValueError(f"Invalid format for {qname}: does not contain enough parts")

                x_part = parts[0][2:]  # Extract the part that should be the number
                print(f"Extracted part: '{x_part}'")  # Debugging line

                if x_part.isdigit() and 1 <= int(x_part) <= 4:
                    print(f"Matched sg{x_part}.trusted.msntv.msn.com")
                    reply = request.reply()
                    reply.add_answer(dnslib.RR(qname, dnslib.QTYPE.A, rdata=dnslib.A("10.0.0.185")))
                    print("Returned server IP - service")
                    return reply
                else:
                    raise ValueError(f"Invalid format for {qname}: extracted part '{x_part}' is not a valid number between 1 and 4")
            except Exception as e:
                print(f"Error processing query: {e}")
                reply = request.reply()
                reply.header.rcode = dnslib.RCODE.SERVFAIL
                return reply

        elif qname in ["headwaiter.msntv.msn.com", "headwaiter.trusted.msntv.msn.com"]:
            print(f"Matched {qname}")
            reply = request.reply()
            reply.add_answer(dnslib.RR(qname, dnslib.QTYPE.A, rdata=dnslib.A("10.0.0.185")))
            reply.add_answer(dnslib.RR(qname, dnslib.QTYPE.TXT, rdata=dnslib.TXT("5554")))
            print("Returned server IP - bootstrap")
            return reply
        
        #elif qname in ["ieatsand.localip"]: This was used for debug
            #print(f"Matched {qname}")
            #reply = request.reply()
            #reply.add_answer(dnslib.RR(qname, dnslib.QTYPE.A, rdata=dnslib.A("10.0.0.185")))
            #reply.add_answer(dnslib.RR(qname, dnslib.QTYPE.TXT, rdata=dnslib.TXT("3000")))
            #print("Returned server IP - lmao")
            #return reply

        else:
            print(f"No match for {qname}")
            reply = request.reply()
            reply.header.rcode = dnslib.RCODE.NXDOMAIN
            return reply

def start_dns_server(host, port):
    resolver = DNSLogger()
    udp_server = dnslib.server.DNSServer(resolver, port=port, address=host)
    udp_server.start_thread()
    return udp_server

if __name__ == "__main__":
    dns_server = start_dns_server(host='10.0.0.185', port=53)
    print(f"DNS server started on 10.0.0.185:53")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        dns_server.stop()
        print("DNS server stopped.")
