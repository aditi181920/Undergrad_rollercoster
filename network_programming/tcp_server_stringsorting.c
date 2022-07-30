/*#include <stdio.h>
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
char menu[200];
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
n = recvfrom(sockfd, (char *)menu, MAXLINE,MSG_WAITALL, ( struct sockaddr *) &cliaddr,&len);
printf("%s\n",menu);


bzero(buffer,sizeof(buffer));
n = recvfrom(sockfd, (char *)buffer, MAXLINE,MSG_WAITALL, ( struct sockaddr *) &cliaddr,&len);
//ssize_t recvfrom(int sockfd, void *buf, size_t len, int flags,struct sockaddr *src_addr, socklen_t *addrlen)
//Receive a message from the socket.
//buffer[n] = '\0';
printf("Client : %s\n", buffer);
int l=strlen(buffer);
//int cnt[26];
//memset(cnt,0,sizeof(cnt));
//for(int i=0,j=l-2;i<=j;i++){
//   cnt[(buffer[i]-'a')]++;
  // int c=buffer[i];
  // buffer[i]=buffer[j];
  // buffer[j]=c;
// }
// int id=0;
// for(int i=0;i<=l-2;i++){
//    while(cnt[id]==0){
//        if(id==26)break;
//        else id++;
//    }
//    buffer[i]=(id+'a');
//    cnt[id]--;
// }
for(int i=0;i<l-2;i++){
   for(int j=0;j<l-2-i;j++){
       if(buffer[j]>buffer[j+1]){
           int c=buffer[j];
           buffer[j]=buffer[j+1];
           buffer[j+1]=c;
       }
    }
 }
 buffer[l-1]='\0';
sendto(sockfd, (const char *)buffer, strlen(buffer),MSG_CONFIRM, (const struct sockaddr *) &cliaddr,len);
//ssize_t sendto(int sockfd,const void *buf, size_t len, int flags,const struct sockaddr *dest_addr, socklen_t addrlen)
//Send a message on the socket
printf("Message sent.\n");
return 0;
}
*/


#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <sys/types.h>
#define MAX 80
#define PORT 8080
#define SA struct sockaddr
// Function designed for chat between client and server.
void func(int sockfd)
{
char buff[MAX],revbuff[MAX],menu[500]="\n**********MENU*********\n1.String sorting\n2.String comparison\n3.String copy\n4.String insertion and deletion from a particular location\n5.Exit\n";
int n;
//write menu to client
write(sockfd,menu,sizeof(menu));
// infinite loop for chat
for (;;) {
    int i,j,n;
    bzero(buff, MAX);
    // read the message from client and copy it in buffer
    //if((n=read(sockfd, buff, sizeof(buff)))==0)break;
    //if (strncmp("exit", buff, 4) == 0) {
    //    printf("Server Exit...\n");
    //    break;
    //}
    //buff[n-1]='\0';
    // print buffer which contains the client contents
    n=read(sockfd, buff, sizeof(buff));
    printf("From client: %s\n ", buff);
    j=0;
    int l=strlen(buff);
    for(int i=0;i<l-2;i++){
        for(int j=0;j<l-2-i;j++){
            if(buff[j]>buff[j+1]){
                int c=buff[j];
                buff[j]=buff[j+1];
                buff[j+1]=c;
            }
         }
     }
    buff[l-1]='\0';
    printf("To client:");
    printf("%s",buff);
    // and send that buffer to client
    write(sockfd, buff, sizeof(buff));
    // if msg contains "Exit" then server exit and chat ended.

    }
}

// Driver function
int main()
{
int sockfd, connfd, len;
struct sockaddr_in servaddr, cli;
// socket create and verification
sockfd = socket(AF_INET, SOCK_STREAM, 0);  

if (sockfd == -1) {
printf("socket creation failed...\n");
exit(0);
}
else
printf("Socket successfully created..\n");
bzero(&servaddr, sizeof(servaddr));
// assign IP, PORT
servaddr.sin_family = AF_INET;
servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
servaddr.sin_port = htons(PORT);
// Binding newly created socket to given IP and verification
if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) {
printf("socket bind failed...\n");
exit(0);
}
else
printf("Socket successfully binded..\n");
// Now server is ready to listen and verification
if ((listen(sockfd, 5)) != 0) {
printf("Listen failed...\n");
exit(0);
}
else
printf("Server listening..\n");
len = sizeof(cli);
// Accept the data packet from client and verification
connfd = accept(sockfd, (SA*)&cli, &len);
if (connfd < 0) {
printf("server acccept failed...\n");
exit(0);
}
else
printf("server acccept the client...\n");
// Function for chatting between client and server
func(connfd);
// After chatting close the socket
close(sockfd);
}

