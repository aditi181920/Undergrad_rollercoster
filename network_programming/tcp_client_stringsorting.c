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
char menu[200]="**********MENU*********\n1.String sorting\n2.String comparison\n3.String copy\n4.String insertion and deletion from a particular location";
char buffer[MAXLINE];
//char *hello = "Hello from client";
struct sockaddr_in servaddr;
// Creating socket file descriptor
if ( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) {
perror("socket creation failed");
exit(EXIT_FAILURE);
}
memset(&servaddr, 0, sizeof(servaddr));
// Filling server information
servaddr.sin_family = AF_INET;
servaddr.sin_port = htons(PORT);
servaddr.sin_addr.s_addr = INADDR_ANY;
int n, len,j=0;


sendto(sockfd, (const char *)menu, strlen(menu),MSG_CONFIRM, (const struct sockaddr *) &servaddr,sizeof(servaddr));

while((buffer[j++]=getchar())!='\n');
buffer[j]='\0';
sendto(sockfd, (const char *)buffer, strlen(buffer),MSG_CONFIRM, (const struct sockaddr *) &servaddr,sizeof(servaddr));
//ssize_t sendto(int sockfd,const void *buf, size_t len, int flags,const struct sockaddr *dest_addr, socklen_t addrlen)
//Send a message on the socket
printf("Message sent.\n");
bzero(buffer,sizeof(buffer));
n = recvfrom(sockfd, (char *)buffer, MAXLINE,MSG_WAITALL, (struct sockaddr *) &servaddr,&len);
//ssize_t recvfrom(int sockfd, void *buf, size_t len, int flags,struct sockaddr *src_addr, socklen_t *addrlen)
//Receive a message from the socket.
//buffer[n] = '\0';
printf("Server : %s\n", buffer);
close(sockfd);
return 0;
}
*/

#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#define MAX 80
#define PORT 8080
#define SA struct sockaddr
void func(int sockfd)
{
char buff[MAX];
char menu[200],choice[200];
int n;
//reading menu
read(sockfd,menu,sizeof(menu));
for (;;) {
    printf("%s",menu);
    //input choice
    printf("Enter your choice:");
    n=0;
    while ((choice[n++] = getchar()) != '\n');
    //find match of choice entered
    if(strncmp("String sorting",choice,14)==0){
        printf("choice 1");
        bzero(buff, sizeof(buff));
        printf("\nEnter the string : ");
        n = 0;
        while ((buff[n++] = getchar()) != '\n');
        write(sockfd, buff, sizeof(buff));
        if ((strncmp(buff, "exit", 4)) == 0) {
            printf("Client Exit...\n");
            break;
        } 
        printf("To server : %s\n",buff);
        bzero(buff, sizeof(buff));
        read(sockfd, buff, sizeof(buff));
        printf("From Server : %s\n", buff);
    }else if(strncmp("String comparison",choice,17)==0){
        printf("choice 2");
    }else if(strncmp("String copy",choice,11)==0){
        printf("choice 3");
    }else if(strncmp("String insertion and deletion from a particular location",choice,56)==0){
        printf("choice 4"); 
        
    }else if(strncmp("Exit",choice,4)==0){
        break;
    }
    else{
        printf("Invalid option!!! please try again");
        }
    }
}
int main()
{
int sockfd, connfd;
struct sockaddr_in servaddr, cli;
// socket create and varification
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
servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");
servaddr.sin_port = htons(PORT);
// connect the client socket to server socket
if (connect(sockfd, (SA*)&servaddr, sizeof(servaddr)) != 0) {
printf("connection with the server failed...\n");
exit(0);
}
else
printf("connected to the server..\n");
// function for chat
func(sockfd);
// close the socket
close(sockfd);
}