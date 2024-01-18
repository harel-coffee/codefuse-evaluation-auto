''' CodefuseEval utility functions '''

import os
from typing import *
import gzip
import json


import os

EVAL_DATASET = {
    "humaneval_python": os.path.join( os.path.dirname( __file__ ), "data", "code_completion", "humaneval_python.jsonl" ),
    "humaneval_python_cn": os.path.join( os.path.dirname( __file__ ), "data", "code_completion", "humaneval_python_cn.jsonl" ),
    "humaneval_js": os.path.join( os.path.dirname( __file__ ), "data", "code_completion", "humaneval_js.jsonl" ),
    "humaneval_java": os.path.join( os.path.dirname( __file__ ), "data", "code_completion", "humaneval_java.jsonl" ),
    "humaneval_go": os.path.join( os.path.dirname( __file__ ), "data", "code_completion", "humaneval_go.jsonl" ),
    "humaneval_rust": os.path.join( os.path.dirname( __file__ ), "data", "code_completion", "humaneval_rust.jsonl" ),
    "humaneval_cpp": os.path.join( os.path.dirname( __file__ ), "data", "code_completion", "humaneval_cpp.jsonl" ),
    "mbpp": os.path.join( os.path.dirname( __file__ ), "data", "nl2code", "mbpp_x.jsonl" ),
    "codeTrans_python_to_java":os.path.join( os.path.dirname( __file__ ), "data", "code_trans", "codeTrans_python_to_java.jsonl" ),
    "codeTrans_python_to_cpp": os.path.join( os.path.dirname( __file__ ), "data", "code_trans", "codeTrans_python_to_cpp.jsonl" ),
    "codeTrans_cpp_to_java": os.path.join( os.path.dirname( __file__ ), "data", "code_trans", "codeTrans_cpp_to_java.jsonl" ),
    "codeTrans_cpp_to_python": os.path.join( os.path.dirname( __file__ ), "data", "code_trans", "codeTrans_cpp_to_python.jsonl" ),
    "codeTrans_java_to_python": os.path.join( os.path.dirname( __file__ ), "data", "code_trans", "codeTrans_java_to_python.jsonl" ),
    "codeTrans_java_to_cpp": os.path.join( os.path.dirname( __file__ ), "data", "code_trans", "codeTrans_java_to_cpp.jsonl" ),

    "codeCompletion_matplotlib": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeCompletion", "Matplotlib", "Matplotlib.jsonl" ),
    "codeCompletion_numpy": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeCompletion", "Numpy", "Numpy.jsonl" ),
    "codeCompletion_pandas": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeCompletion", "Pandas", "Pandas.jsonl" ),
    "codeCompletion_pytorch": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeCompletion", "Pytorch", "Pytorch.jsonl" ),
    "codeCompletion_scipy": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeCompletion", "Scipy", "Scipy.jsonl" ),
    "codeCompletion_sklearn": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeCompletion", "Sklearn", "Sklearn.jsonl" ),
    "codeCompletion_tensorflow": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeCompletion", "Tensorflow", "Tensorflow.jsonl" ),

    "codeInsertion_matplotlib": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeInsertion", "Matplotlib", "Matplotlib.jsonl" ),
    "codeInsertion_numpy": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeInsertion", "Numpy", "Numpy.jsonl" ),
    "codeInsertion_pandas": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeInsertion", "Pandas", "Pandas.jsonl" ),
    "codeInsertion_pytorch": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeInsertion", "Pytorch", "Pytorch.jsonl" ),
    "codeInsertion_scipy": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeInsertion", "Scipy", "Scipy.jsonl" ),
    "codeInsertion_sklearn": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeInsertion", "Sklearn", "Sklearn.jsonl" ),
    "codeInsertion_tensorflow": os.path.join( os.path.dirname( __file__ ), "data", "codedatascience", "CodeInsertion", "Tensorflow", "Tensorflow.jsonl" )

}

DATASET_SUPPORT = {
    "humaneval_python": ["code_completion"],
    "humaneval_python_cn": ["code_completion"],
    "humaneval_js": ["code_completion"],
    "humaneval_java": ["code_completion"],
    "humaneval_go": ["code_completion"],
    "humaneval_rust": ["code_completion"],
    "humaneval_cpp": ["code_completion"],
    "mbpp": ["nl2code"],
    "codeTrans_python_to_java":["code_trans"],
    "codeTrans_python_to_cpp": ["code_trans"],
    "codeTrans_cpp_to_java": ["code_trans"],
    "codeTrans_cpp_to_python": ["code_trans"],
    "codeTrans_java_to_python": ["code_trans"],
    "codeTrans_java_to_cpp": ["code_trans"],
    "codeCompletion_matplotlib":["codescience"],
    "codeCompletion_numpy":["codescience"],
    "codeCompletion_pandas":["codescience"],
    "codeCompletion_pytorch":["codescience"],
    "codeCompletion_scipy":["codescience"],
    "codeCompletion_sklearn":["codescience"],
    "codeCompletion_tensorflow":["codescience"],
    "codeInsertion_matplotlib":["codescience"],
    "codeInsertion_numpy":["codescience"],
    "codeInsertion_pandas":["codescience"],
    "codeInsertion_pytorch":["codescience"],
    "codeInsertion_scipy":["codescience"],
    "codeInsertion_sklearn":["codescience"],
    "codeInsertion_tensorflow":["codescience"]
}


DATASET_LANGUAGE = {
    "humaneval_python": "python",
    "humaneval_python_cn": "python",
    "humaneval_js": "js",
    "humaneval_java": "java",
    "humaneval_go": "go",
    "humaneval_rust": "rust",
    "humaneval_cpp": "cpp",
    "mbpp": "python",
    "codeTrans_python_to_java":"java",
    "codeTrans_python_to_cpp": "cpp",
    "codeTrans_cpp_to_java": "java",
    "codeTrans_cpp_to_python": "python",
    "codeTrans_java_to_python": "python",
    "codeTrans_java_to_cpp": "cpp",
    "codeCompletion_matplotlib":"python",
    "codeCompletion_numpy":"python",
    "codeCompletion_pandas":"python",
    "codeCompletion_pytorch":"python",
    "codeCompletion_scipy":"python",
    "codeCompletion_sklearn":"python",
    "codeCompletion_tensorflow":"python",
    "codeInsertion_matplotlib":"python",
    "codeInsertion_numpy":"python",
    "codeInsertion_pandas":"python",
    "codeInsertion_pytorch":"python",
    "codeInsertion_scipy":"python",
    "codeInsertion_sklearn":"python",
    "codeInsertion_tensorflow":"python"
}

# model decode strategy
ALL_DECODE_MODE = ["greedy", "beams", "dosample"]

# import lib for current language
IMPORT_HELPER = {
    "python": [
        "import math",
        "import unittest",
        "import re",
        "import sys",
        "import copy",
        "import datetime",
        "import itertools",
        "import collections",
        "import heapq",
        "import statistics",
        "import functools",
        "import hashlib",
        "import numpy",
        "import numpy as np",
        "import string",
        "from typing import *",
        "from collections import *",
    ],
    "go": [
        "math",
        "strings",
        "fmt",
        "strconv",
        "time",
        "bytes",
        "regexp",
        "sort",
        "math/rand",
        "crypto/md5",
    ],
    "cpp": [
        "#include<stdlib.h>",
        "#include<algorithm>",
        "#include<math.h>",
        "#include<stdio.h>",
        "#include<vector>",
        "#include<string>",
        "#include<climits>",
        "#include<cstring>",
        "#include<iostream>",
        "#include <stdexcept>",
    ],
    "java": [
        "import java.io.*;",
        "import java.lang.*;",
        "import java.util.*;",
        "import java.math.*;",

    ]
}


#eval dataset registry, support jsonlfile or jsonl.gz file

def read_dataset(
        data_file: str = None,
        dataset_type: str = "humaneval",
        num_shot=None,
) -> Dict:
    """
    read dataset file and return as a dictionary
    """
    if num_shot is not None:
        print(f"{num_shot}-shot setting...")
    if "humaneval" in dataset_type.lower():
        if data_file is None:
            current_path = os.path.dirname(os.path.abspath(__file__))
            # 补充一个默认数据集
            data_file = os.path.join(current_path, "data", "code_completion", "humaneval_python.jsonl")
        dataset = {task["task_id"]: task for task in stream_jsonl(data_file)}
    else:
        raise f"Dataset: {dataset_type} not supported."

    return dataset


def stream_jsonl(filename: str) -> Iterable[Dict]:
    """
    Parses each jsonl line and yields it as a dictionary
    """
    if filename.endswith(".gz"):
        with open(filename, "rb") as gzfp:
            with gzip.open(gzfp, "rt") as fp:
                for line in fp:
                    if any(not x.isspace() for x in line):
                        yield json.loads(line)
    else:
        with open(filename, "r") as fp:
            for line in fp:
                if any(not x.isspace() for x in line):
                    yield json.loads(line)

def is_contain_chinese(check_str):
    """
    Determine whether the string contains Chinese characters
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def get_gopackages(code):
    """
    The main purpose is to extract go package information and then diagnose the usage of the package.
    If the current package is not used, delete it directly to improve the compilation pass rate.
    Args:
    code: The golang code.
    Returns:
    The golang code import libs list.
    """
    code_line = code.split("\n")
    packages = []
    start_import = False
    for line in code_line:
        if "import" in line:
            if "(" in line:
                start_import = True
                continue
            else:
                packages.append( line.split( " " )[1][1:-1] )
        if start_import:
            if ")" in line:
                start_import = False
                continue
            temp_line = line.split( "," )[0].strip()
            if temp_line=="":
                continue
            if temp_line.startswith( "\"" ) or temp_line.startswith( "\'" ):
                if temp_line.endswith( "\"" ) or temp_line.endswith( "\'" ):
                    packages.append( temp_line[1:-1] )
                else:
                    packages.append( temp_line[1:] )
            else:
                packages.append(line.split(",")[0].strip())
    return packages

def write_jsonl(data, output_path):
    """
    write data in a jsonl file
    """
    output_dir = os.path.dirname(output_path)
    if output_dir is not None and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    write_data = []
    for item in data:
        try:
            data = json.dumps(item, ensure_ascii=False)
            write_data.append(data)
        except Exception as e:
            print(f"fail to dumps lines,the line is {item}")
    with open(output_path, "w", encoding='utf-8') as f:
        f.write("\n".join(write_data))