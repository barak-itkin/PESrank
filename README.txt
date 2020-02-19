PESrank

This is a Python implementation.

The main function is PESrank.main:
Input:
   a username  
   a password   
   the path of the five text files: a1.txt, a2.txt, a3.txt, a4.txt, a5.txt. 

PESrank.main creates a new file. This file is located at directory "out" at the given path. 
The file contains the following details in one line:
the given username, the strength of the given password, the file creation time.
   

An example for usage:
PESrank.main("adam","password123","path")


Copyright (C) Liron David and Avishai Wool, 2020. All rights reserved.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

If you find this software useful, we ask that you cite our paper:

@article{david2019context,
  title={Context Aware Password Guessability via Multi-Dimensional Rank Estimation},
  author={David, Liron and Wool, Avishai},
  journal={arXiv preprint arXiv:1912.02551},
  year={2019}
}


Technical report https://arxiv.org/abs/1912.02551


Send comments / requests / patches to:
   Liron David <lirondavid@gmail.com>
  

