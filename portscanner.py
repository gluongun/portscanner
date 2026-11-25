import asyncio


async def portscan(host, port, timeout = 1.0):
    """attempting TCP connection asynciously"""
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(host, port),
            timeout =timeout

        )

        writer.close()
        await writer.wait_closed()
        return port, "open"


    except(asyncio.TimeoutError, ConnectionResetError, OSError):
        return port, "closed"


async def main(host, ports):
    tasks =[portscan(host, port) for port in ports]
    results = await asyncio.gather(*tasks)

    for port, status in results:
        if status == "open":
            print(f"port {port}: OPEN")


if __name__ == "__main__":
    target_ports =range(1, 1025)
    asyncio.run(main("127.0.0.1", target_ports))


