require 'socket'
server = TCPServer.new 8080

while session = server.accept
  request = session.gets
  puts request

  session.print "HTTP/1.1 200\r\n"
  session.print "Content-Type: text/html\r\n"
  session.print "\r\n"
  session.print "Hello world! my IP is #{IPSocket.getaddress(Socket.gethostname)}"

  session.close
end