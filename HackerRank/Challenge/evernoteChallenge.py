__author__ = 'san'
__hacker_rank = 'https://www.hackerrank.com/sanaltsk'
__link__ = 'https://www.hackerrank.com/contests/evernote-coding-challenge/challenges/evernote-search'

import xml.etree.ElementTree as ET
s = """<note>
  <guid>C93939E4-A607-4EF7-80C1-A1D732C78C87</guid>
  <created>2014-04-16T14:23:11Z</created>
  <tag>armadillo</tag>
  <tag>bonobo</tag>
  <tag>cormorant</tag>
  <content>
    Let us get things started with a coarse-grained overview of the physical makeup of
    the Evernote service. I will not go into a lot of detail on each component here;
    we will aim to talk about the interesting bits in separate posts later.

    Starting at the top-left corner of the diagram, all stats as of May 17th, 2011...

    Networking: Virtually all traffic to and from Evernote comes to www.evernote.com
    via HTTPS port 443. This includes all "web" activity, but also all client
    synchronization via our Thrift-based service API. Altogether, that produces up to
    150 million HTTPS requests per day, with peak traffic around 250
    Mbps. (Unfortunately for our semi-nocturnal Operations team, this daily peak tends
    to arrive around 6:30 am, Pacific time.)
    We use BGP to direct traffic through fully independent network feeds from our
    primary (NTT) and secondary (Level 3) providers. This is filtered through Vyatta
    on the way to the new A10 load balancers that we deployed in January when we hit
    the limit of SSL performance for our old balancers. We are comfortably handling
    existing traffic using one AX 2500 plus a failover box, but we are preparing to
    test their N+1 configuration in our staging cluster to prepare for future growth.
  </content>
</note> """


root = ET.fromstring(s)

print dir(root)

print root[0].text
print root[5].text


for i in range()
