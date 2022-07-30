#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#define PORT 8080
#define MAXLINE 1024
// Driver code
int main() {
int sockfd;
char buffer[MAXLINE];
//char *hello = "Hello from server";
struct sockaddr_in servaddr, cliaddr;
// Creating socket file descriptor using socket function
//int socket(int domain, int type, int protocol)
if ( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) {
perror("socket creation failed");
exit(EXIT_FAILURE);
}
//SOCK_DGRAM is used for connectionless protocol
memset(&servaddr, 0, sizeof(servaddr));
memset(&cliaddr, 0, sizeof(cliaddr));
// Filling server information
servaddr.sin_family = AF_INET; // AF_INET family is for IPv4
servaddr.sin_addr.s_addr = INADDR_ANY;
servaddr.sin_port = htons(PORT); //htons: host to network bytes in short format
// Bind the socket with the server address
//int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen)
//Assigns address to the unbound socket.
if ( bind(sockfd, (const struct sockaddr *)&servaddr,sizeof(servaddr)) < 0 )
{
perror("bind failed");
exit(EXIT_FAILURE);
}
int len, n;
bzero(buffer,sizeof(buffer));
n = recvfrom(sockfd, (char *)buffer, MAXLINE,MSG_WAITALL, ( struct sockaddr *) &cliaddr,&len);
//ssize_t recvfrom(int sockfd, void *buf, size_t len, int flags,struct sockaddr *src_addr, socklen_t *addrlen)
//Receive a message from the socket.
//buffer[n] = '\0';
printf("Client : %s\n", buffer);
int l=strlen(buffer);
for(int i=0,j=l-2;i<j;i++,j--){
   int c=buffer[i];
   buffer[i]=buffer[j];
   buffer[j]=c;
 }
 buffer[l-1]='\0';
sendto(sockfd, (const char *)buffer, strlen(buffer),MSG_CONFIRM, (const struct sockaddr *) &cliaddr,len);
//ssize_t sendto(int sockfd,const void *buf, size_t len, int flags,const struct sockaddr *dest_addr, socklen_t addrlen)
//Send a message on the socket
printf("Message sent.\n");
return 0;
}