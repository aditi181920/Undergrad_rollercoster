#include <stdio.h> 
#include <netdb.h> 
#include <netinet/in.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <sys/types.h> 
#include <unistd.h>
#include<stdlib.h>
#define MAX 1000
#define PORT 8080 
#define SA struct sockaddr 
char res[MAX];
char* str_sort(char* str)
{
	bzero(res,MAX);
	int l=strlen(str);
	//printf("length=%d\n",l);
	char words[50][100];
	int i,j,k;
	for(i=0,j=0,k=0;j<l;j++)
	{
		if(str[j]==' '|| str[j]=='\n')
		{
			words[i][k]='\0';
			i++;
			k=0;
		}
		else
		{
			words[i][k++]=str[j];
		}
	}
	int c=i;
	//printf("Words=%d\n",i);
	/*for(j=0;j<c;j++)
	{
		printf("%s\n",words[j]);
	}*/
	for(i=0;i<c;i++)
	{
		for(j=0;j<c-i-1;j++)
		{
			if(strcmp(words[j],words[j+1])>0)
			{
				char temp[100];
				strcpy(temp,words[j]);
				strcpy(words[j],words[j+1]);
				strcpy(words[j+1],temp);
			}
		}
	}
	/*for(j=0;j<c;j++)
	{
		printf("%s\n",words[j]);
	}*/
	j=0;
	for(i=0;i<c;i++)
	{
		l=strlen(words[i]);
		for(k=0;k<l;k++)
		{
			res[j++]=words[i][k];
		}
		res[j++]=' ';
	}
	res[j++]='\n';
	res[j++]='\0';
	//printf("Result=%s\n",res);
	return (char*)res;
	
}
char* str_copy(char* str)
{
	bzero(res,MAX);
	int i=0;
	for(i=0;i<strlen(str);i++)
	{
		res[i]=str[i];
	}
	return res;
}
char* str_cmp(char* str1,char* str2)
{
	char *ptr;
	int r=strcmp(str1,str2);
	if(r==0)
	ptr="Both strings are equal\n";
	else if(r>0)
	ptr="First string is alphabetically bigger\n";
	else
	ptr="Second string is alphabetically bigger\n";
	return (char*)ptr;
}
char* str_ins(char* buff,char* loc,char* str)
{
	//char* ptr="hi\n";
	int l1=strlen(buff);
	int l2=strlen(str);
	bzero(res,MAX);
	int i,j,k=0;
	char *t;
	long p=strtol(loc,&t,10);
	if(p<=l1)
	{
		//printf("p=%ld\n",p);
		for(i=0;i<p-1;i++)
		{
			res[k++]=buff[i];
		}
		for(j=0;j<l2-1;j++)
		{
			res[k++]=str[j];
		}
		for(;i<l1-1;i++)
		{
			res[k++]=buff[i];
		}
		//printf("result=%s\n",res);
		res[k++]='\n';
		
	}
	else
	{
		for(i=0;i<l1-1;i++)
		{
			res[k++]=buff[i];
		}
		for(i=0;i<l2-1;i++)
		{
			res[k++]=str[i];
		}
		//printf("result=%s\n",res);
		res[k++]='\n';
	}
	return (char*)res;
}
char* str_del(char* buff,char* loc,char * len)
{
	//char* ptr="bye\n";
	int l=strlen(buff);
	bzero(res,MAX);
	int i,j,k=0;
	char *t;
	long p=strtol(loc,&t,10);
	long l1=strtol(len,&t,10);
	//printf("p=%ld  l1=%ld\n",p,l1);
	if(p<=l)
	{
		//printf("p=%ld\n",p);
		for(i=0;i<p-1;i++)
		{
			res[k++]=buff[i];
			//printf("%c\n",buff[i]);
		}
		i+=l1;
		for(;i<l-1;i++)
		{
			res[k++]=buff[i];
			//printf("%c\n",buff[i]);
		}
		//printf("result=%s\n",res);
		res[k++]='\n';
		
	}
	else
	{
		for(i=0;i<l-1;i++)
		{
			res[k++]=buff[i];
		}
		//printf("result=%s\n",res);
		res[k++]='\n';
	}
	return (char*)res;
}
void func(int sockfd)
{
	char buff[MAX];
	int n;
	for(;;)
	{
		bzero(buff,MAX);
		read(sockfd,buff,sizeof(buff));
		printf("From client:%s",buff);
		if(strncmp("exit",buff,4)==0)
		{
			printf("Server Exit...\n");
			break;
		}
		char choice_list[MAX]="Select one option\n1. String sorting\n2. String comparison\n3. String copy\n4. Stringinsertion and deletion from a particular location\n";
		write(sockfd,choice_list,sizeof(choice_list));
		char choice[MAX];
		read(sockfd,choice,sizeof(choice));
		printf("Client choice=%s",choice);
		char *result;
		result='\0';
		if(strncmp(choice,"1",1)==0)
		{
			//printf("Your choice=11\n");
			result=str_sort(buff);
			printf("Sorted string=%s\n",result);
			//printf("Size=%d",(int)strlen(result));
			
		}
		else if(strncmp(choice,"2",1)==0)
		{
			//printf("Your choice=22\n");
			char buff1[MAX];
			bzero(buff1,MAX);
			char message[MAX]="Enter one more string for comparison:";
			write(sockfd,message,sizeof(message));
			read(sockfd,buff1,sizeof(buff1));
			//printf("Bufer=%s",buff1);
			result=str_cmp(buff,buff1);
			bzero(buff1,MAX);
			printf("Comparison result=%s\n",result);
			//printf("Size=%d",(int)strlen(result));
			
		}
		else if(strncmp(choice,"3",1)==0)
		{
			//printf("Your choice=33\n");
			result=str_copy(buff);
			printf("String copy=%s\n",result);
			//printf("Size=%d",(int)strlen(result));
		}
		else if(strncmp(choice,"4",1)==0)
		{
			//printf("Your choice=44\n");
			char buff1[MAX];
			bzero(buff1,MAX);
			char message[MAX]="Enter a for insertion and b for deletion:";
			write(sockfd,message,sizeof(message));
			read(sockfd,buff1,sizeof(buff1));
			char buff3[MAX];
			bzero(buff3,MAX);
			if(strncmp(buff1,"a",1)==0)
			{
				char message2[MAX]="Enter string to be inserted:";
				write(sockfd,message2,sizeof(message2));
				read(sockfd,buff3,sizeof(buff3));
			}
			if(strncmp(buff1,"b",1)==0)
			{
				char message2[MAX]="Enter length of string to be deleted:";
				write(sockfd,message2,sizeof(message2));
				read(sockfd,buff3,sizeof(buff3));
			}
			char buff2[MAX];
			bzero(buff2,MAX);
			char message1[MAX]="Enter location:";
			write(sockfd,message1,sizeof(message1));
			read(sockfd,buff2,sizeof(buff2));
			if(strncmp(buff1,"a",1)==0)
			{
				result=str_ins(buff,buff2,buff3);
				printf("Result=%s\n",result);
			}
			if(strncmp(buff1,"b",1)==0)
			{
				result=str_del(buff,buff2,buff3);
				printf("Result=%s\n",result);
			}
			
			
		}
		else
		{
			result="Wrong choice\n";
		}
		char fin_res[MAX];
		bzero(fin_res,MAX);
		int i;
		for(i=0;i<strlen(result);i++)
		{
			fin_res[i]=result[i];
		}
		write(sockfd,fin_res,sizeof(fin_res));
	}
}
int main()
{
	int sockfd,connfd,len;
	struct sockaddr_in servaddr,cli;
	sockfd=socket(AF_INET,SOCK_STREAM,0);
	if(sockfd==-1)
	{
		printf("Socket creation failed...\n");
		exit(0);
	}
	else
	{
		printf("Socket successfully created..\n"); 
	}
	bzero(&servaddr, sizeof(servaddr)); 
	servaddr.sin_family = AF_INET; 
    	servaddr.sin_addr.s_addr = htonl(INADDR_ANY); 
	servaddr.sin_port = htons(PORT);
	if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) 
	{ 
        	printf("socket bind failed...\n"); 
        	exit(0); 
    	} 
    	else
        {
        	printf("Socket successfully binded..\n"); 
        }
        
        if ((listen(sockfd, 5)) != 0) 
        { 
        	printf("Listen failed...\n"); 
        	exit(0); 
    	} 
	else
	{
        	printf("Server listening..\n"); 
        }
    	len = sizeof(cli); 
     	connfd = accept(sockfd, (SA*)&cli, &len); 
    	if (connfd < 0) 
    	{ 
        	printf("server acccept failed...\n"); 
        	exit(0); 
    	} 
    	else
        {
        	printf("server acccept the client...\n"); 
        }  
        func(connfd);
        close(sockfd);           
}

