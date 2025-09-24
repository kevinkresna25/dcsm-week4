#!/usr/bin/env bash
set -e

if command -v docker compose &> /dev/null; then
    DC="docker compose"
elif command -v docker-compose &> /dev/null; then
    DC="docker-compose"
else
    echo "❌ docker compose or docker-compose not found!"
    exit 1
fi

COMPOSE_FILE="docker-compose.yml"

# Help Function
usage() {
    echo "Usage: $0 {up|down|status} [all|rmi|grpc-java|grpc-python ...]"
    echo
    echo "Examples:"
    echo "  $0 up all                # Start semua service"
    echo "  $0 up rmi                # Start hanya RMI"
    echo "  $0 up grpc-java          # Start hanya gRPC Java"
    echo "  $0 up grpc-python        # Start hanya gRPC Python"
    echo "  $0 up rmi grpc-java      # Start gabungan RMI + gRPC Java"
    echo "  $0 down                  # Stop semua container"
    echo "  $0 status                # Lihat status container"
}

# Subcommand
CMD=$1
shift || true

case "$CMD" in
    up)
        if [ $# -eq 0 ]; then
            usage
            exit 1
        fi

        if [ "$1" == "all" ]; then
            echo "🚀 Starting ALL profiles (rmi, grpc-java, grpc-python)..."
            $DC -f $COMPOSE_FILE \
                --profile rmi \
                --profile grpc-java \
                --profile grpc-python \
                up -d --build
        else
            echo "🚀 Starting profiles: $@ ..."
            ARGS=""
            for p in "$@"; do
                ARGS="$ARGS --profile $p"
            done
            $DC -f $COMPOSE_FILE $ARGS up -d --build
        fi

        echo "✅ Services started. Current status:"
        $DC -f $COMPOSE_FILE ps
        ;;

    down)
        echo "🛑 Stopping all services..."
        $DC -f $COMPOSE_FILE down
        echo "✅ All services stopped."
        ;;

    status)
        echo "📊 Container status:"
        $DC -f $COMPOSE_FILE ps
        ;;

    *)
        usage
        exit 1
        ;;
esac
