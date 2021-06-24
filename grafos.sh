# Instalando o virtualvenv no linux
# chmod +x grafos.sh

GREEN="\033[1;32m";
BLUE="\033[1;34m";
RESET="\033[0m";

echo "${BLUE}> [instalation] Instalation pip${RESET}";
sudo apt-get install python3-pip;

echo "${BLUE}> [instalation] Instaling virtualenv using pip3${RESET}";
sudo pip3 install virtualenv 

echo "${BLUE}> [instalation] Creating a virtual environment${RESET}";
virtualenv venv 


echo "${GREEN}> Finished${RESET}";