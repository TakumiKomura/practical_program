// Fast Fourier Transformを行う
// 偶数行と奇数行に分割して再帰的に計算する分割統治法を用いることで計算量をO(NlogN)にする
#include<stdio.h>
#include<math.h>
#include<complex.h>

#define N 1024

// Fast Fourier Transform
void FFT(double complex inputArray[], double complex outputArray[], int n)
{
    // 再帰の終わり
    if (n==1){
        // 出力 = 入力
        outputArray[0] = inputArray[0];
    }else{
        // 偶数行を計算
        double complex evenInput[N];
        for (int i = 0; i < n/2;i++){
            evenInput[i] = inputArray[i] + inputArray[i + n/2];
        }
        double complex evenOutput[N];
        FFT(evenInput, evenOutput, n / 2);

        // 奇数行を計算
        double complex oddInput[N];
        double complex w_factor;
        for (int i = 0; i < n/2;i++){
            w_factor = cexp(-2 * M_PI * i * I / n); // w = exp(-j(2*pi*i/n))
            oddInput[i] = w_factor * (inputArray[i] - inputArray[i + n/2]);
        }
        double complex oddOutput[N];
        FFT(oddInput, oddOutput, n / 2);

        // 偶数行と奇数行を併合
        for (int i = 0; i < n / 2;++i){
            outputArray[2*i] = evenOutput[i];
            outputArray[2*i+1] = oddOutput[i];
        }
    }
}

// 複素数を出力する関数
void cprint(double complex z)
{
  printf("%g + %gi\n", creal(z), cimag(z));
}

// 複素数型配列の要素を入力する関数
void scanArray(double complex array[], int n)
{
    int i;
    double tmp;
    for (i = 0; i < n;++i){
        scanf("%le", &tmp);
        array[i] = tmp + 0 * I;
    }
}

// 複素数型配列を出力する関数
void printArray(double complex array[], int n)
{
    int i;
    for (i = 0; i < n;++i){
        cprint(array[i]);
    }
}

int main()
{
    int n;
    double complex inputArray[N];
    double complex fourierArray[N];

    printf("input n: ");
    scanf("%d", &n);
    printf("input n real numbers:\n");
    scanArray(inputArray, n);

    FFT(inputArray, fourierArray, n);

    printf("\ntransformed n numbers:\n");
    printArray(fourierArray, n);
}