# PESrank

This is a python implementation of PESrank, for the technical report
in https://arxiv.org/abs/1912.02551.

## Code overview
The main function is `PESrank.main`, which accepts three paramters:

1. A username  
2. A password   
3. the path of the five text files: a1.txt, a2.txt, a3.txt, a4.txt, a5.txt. 

`PESrank.main` creates a new file. This file is located at directory "out" at the given path. 
The file contains the following details in one line:
the given username, the strength of the given password, the file creation time.
   
An example for usage:
```
PESrank.main("adam","password123","path")
```

## License
This program is developped by Liron David and Avishai Wool, and it is licensed
under GPLv2 - See [license.txt](license.txt) for more information.

## Citing us
If you find this software useful, we ask that you cite our paper:

```
@article{david2019context,
  title={Context Aware Password Guessability via Multi-Dimensional Rank Estimation},
  author={David, Liron and Wool, Avishai},
  journal={arXiv preprint arXiv:1912.02551},
  year={2019}
}
```

## Contact details
Send comments / requests / patches to: Liron David <lirondavid@gmail.com>