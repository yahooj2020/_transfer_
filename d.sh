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
# if [ -e "/home/t.txt" ] 
# then    
#     if $1='-h'; then 
#         echo 'OK'
#     else
#         echo '1'
#     fi 

    # if "${@:2:1}"="t.txt"; then 
    #     echo 'OK'
    # else
    #     echo '2'
    # fi 
# fi 
# echo "${@:1:1}"
# echo "${@:2:1}"

for i in $@
do
    # echo $count: $i
    # count=$[ $count + 1 ]
    echo $i
done
# if ($*) = ('-h''./t.txt')
# then   
#     echo 'OK'
# else
#     echo '1'
# fi 

# shell  逐个比较两个数组中的每个值
# ChatGPT
# 要逐个比较两个数组中的每个值，可以使用循环结构来遍历数组并进行比较。以下是一个示例，演示了如何逐个比较两个数组中的每个值：

# shell
# Copy code
# #!/bin/bash

# # 第一个数组
# array1=("apple" "banana" "orange" "grape")

# # 第二个数组
# array2=("apple" "kiwi" "orange" "grape")

# # 获取数组长度
# length=${#array1[@]}

# # 遍历数组并逐个比较值
# for ((i=0; i<$length; i++))
# do
#     # 获取当前索引的值
#     value1=${array1[i]}
#     value2=${array2[i]}
    
#     # 比较两个值
#     if [ "$value1" = "$value2" ]; then
#         echo "值相等: $value1"
#     else
#         echo "值不相等: $value1 和 $value2"
#     fi
# done
# 在上面的示例中，定义了两个数组array1和array2，然后使用${#array1[@]}获取数组的长度。通过循环遍历数组的索引，依次获取两个数组中相同索引位置的值，并进行比较。如果值相等，则输出"值相等: $value1"，否则输出"值不相等: $value1 和 $value2"。

# 请注意，在进行值的比较时，使用=号进行字符串比较。如果要进行数字比较，可以使用-eq、-ne等运算符。你可以根据具体需求修改比较的方式。






#!/bin/bash

# 第一个数组

# 第二个数组
array1=("-h" "t.txt")
array2=("${@:1:1}" "${@:2:1}")

# 获取数组长度
length=${#array1[@]}

# 遍历数组并逐个比较值
for ((i=0; i<$length; i++))
do
    # 获取当前索引的值
    value1=${array1[i]}
    value2=${array2[i]}
    
    # 比较两个值
    if [ "$value1" = "$value2" ]; then
        echo "值相等: $value1"
    else
        echo "值不相等: $value1 和 $value2"
    fi
done
