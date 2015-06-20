#include <stdio.h> //standart I/O
#include <sys/types.h> //data types
#include <sys/mman.h>  //memory management declarations
#include <fcntl.h> //file control options
#include <stdlib.h> //standart library definitions
#include <unistd.h>  //standard symbolic constants and types

int main(int argc, char const *argv[])
{
	int fd = 0;
	char * p = NULL;
	char * name = NULL;
	unsigned int file_size = 0;
	unsigned int file_offset = 0;
	unsigned int file_value = 0;

	if (argc < 2)
	{
		printf("[-] Hata: eksik arguman\n");
		printf("[?] ./fuzzer <DosyaBoyutu> <DosyaOffseti> <Deger> <DosyaIsmi>\n");
		return 1;
	} else {
		file_size = atol(argv[1]);     //
		file_offset = atol(argv[2]);
		file_value = atol(argv[3]);
		name = argv[4];
	}

	//dosya aciliyor
	fd = open(name, O_RDWR);  // O_RDWR -> open for reading and writing
	if (fd < 0)
	{
		perror("open");
		exit(1);
	}

	//mmap dosyası
	//map pages of memory 

	p = mmap(0, file_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
	if ((int) p == -1)
	{
		perror("mmap");
		close(fd);
		exit(1);
	}

	//dosya degisimi

	printf("[+] offset: 0x%08x (deger: 0x%08x)\n", file_offset, file_value);
	fflush(stdout);
	p[file_offset] = file_value;

	close(fd);

	//unmap pages of memory
	munmap(p, file_size);

	return 0;
}
