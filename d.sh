#!/bin/bash
# echo 参数数量: $#

# then

#     echo `cat  $2 `

# fi


# read -p './t.txt' filepath 

# if [ -e $filepath ]
# then
    
#     # echo `cat t.txt `
#     # echo '\n'
# else 
    
#     # echo '\n'
# fi 
param_array=('-h','./t.txt')
# if [ ! -f './t.txt' ]
# then
#     echo '2'
# else
#     if [ $# -eq 2 ];then 
#         for i in $@
#         do
#             echo $count: $i
#             count=$[ $count + 1 ]
#         done
#         # echo `cat $2`
#     fi 
# fi 
echo "${param_array[0]}"
echo "${param_array[1]}"
echo "${param_array}"
echo $param_array
echo $@