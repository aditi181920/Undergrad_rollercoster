#include <netdb.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <unistd.h>
#include <arpa/inet.h>
#define MAX 1000
#define PORT 8080 
#define SA struct sockaddr 
void func(int sockfd)
{
	char buff[MAX];
	int n;
	for(;;)
	{
		bzero(buff,MAX);
		printf("Enter string to be sent to server:");
		n=0;
		while((buff[n++]=getchar())!='\n');
		write(sockfd,buff,sizeof(buff));
		if(strncmp("exit",buff,4)==0)
		{
			printf("Client Exit...\n");
			break;
		}
		bzero(buff,sizeof(buff));
		read(sockfd,buff,sizeof(buff));
		printf("Message from Server\n");
		printf("%s",buff);
		bzero(buff,MAX);
		char choice[MAX];
		n=0;
		printf("Choice:");
		while((choice[n++]=getchar())!='\n');
		write(sockfd,choice,sizeof(choice));
		if(strncmp(choice,"2",1)==0)
		{
			read(sockfd,buff,sizeof(buff));
			printf("%s",buff);
			bzero(buff,MAX);
			n=0;
			while((buff[n++]=getchar())!='\n');
			write(sockfd,buff,sizeof(buff));
			bzero(buff,MAX);
		}
		if(strncmp(choice,"4",1)==0)
		{
			read(sockfd,buff,sizeof(buff));
			printf("%s",buff);
			bzero(buff,MAX);
			n=0;
			while((buff[n++]=getchar())!='\n');
			write(sockfd,buff,sizeof(buff));
			if(strncmp(buff,"a",1)==0)
			{
				bzero(buff,MAX);
				read(sockfd,buff,sizeof(buff));
				printf("%s",buff);
				bzero(buff,MAX);
				n=0;
				while((buff[n++]=getchar())!='\n');
				write(sockfd,buff,sizeof(buff));
				
			}
			if(strncmp(buff,"b",1)==0)
			{
				bzero(buff,MAX);
				read(sockfd,buff,sizeof(buff));
				printf("%s",buff);
				bzero(buff,MAX);
				n=0;
				while((buff[n++]=getchar())!='\n');
				write(sockfd,buff,sizeof(buff));
				
			}
			read(sockfd,buff,sizeof(buff));
			printf("%s",buff);
			n=0;
			bzero(buff,MAX);
			while((buff[n++]=getchar())!='\n');
			write(sockfd,buff,sizeof(buff));
			bzero(buff,MAX);
		}
		bzero(buff,MAX);
		read(sockfd,buff,sizeof(buff));
		printf("Result=%s",buff);
		printf("\n");
		//printf("Size=%d",(int)strlen(buff));
		
	}
}  
int main() 
{
	int sockfd, connfd; 
    	struct sockaddr_in servaddr, cli; 
    	sockfd = socket(AF_INET, SOCK_STREAM, 0); 
    	if (sockfd == -1) 
    	{ 
        	printf("socket creation failed...\n"); 
        	exit(0); 
    	} 
    	else
    	{
        	printf("Socket successfully created..\n"); 
        }
    	bzero(&servaddr, sizeof(servaddr)); 
    	servaddr.sin_family = AF_INET; 
    	servaddr.sin_addr.s_addr = inet_addr("127.0.0.1"); 
    	servaddr.sin_port = htons(PORT); 
    	if (connect(sockfd, (SA*)&servaddr, sizeof(servaddr)) != 0) 
    	{ 
        	printf("connection with the server failed...\n"); 
        	exit(0); 
    	} 
    	else
        {
        	printf("connected to the server..\n"); 
        }
        func(sockfd);
        close(sockfd);
} 
