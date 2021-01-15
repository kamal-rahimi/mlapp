
# Install Docker if not installed
if ! command -v docker > /dev/null
then
    echo "Installing docker ..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    rm get-docker.sh
else
    echo "docker is already insatlled"
fi

# Install docker-compose if not installed
if  ! command -v docker-compose > /dev/null
then
    echo "Installing docker-compose ..."
    curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
else
    echo "docker-compose is already insatlled"
fi

# Stop earlier runs of the app
echo "Stopping and remvoing previous docker containers ..."
docker-compose down

# strat running the app
echo "building docker containers ..."
docker-compose up --build -d