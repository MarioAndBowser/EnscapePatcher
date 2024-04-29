import asyncio
import threading
import json
from typing import Any, Callable, Self

from mitmproxy import http
from mitmproxy.addons import default_addons, script
from mitmproxy.master import Master
from mitmproxy.options import Options


class Addon:
    def __init__(self) -> None:
        print("😈 Patch initialized")

    def response(self, flow: http.HTTPFlow) -> None:
        if flow.response:
            current_url = flow.request.pretty_url

            if current_url == 'https://api2.enscape3d.com/lic/api/license/data':
                content = json.loads(flow.response.get_text())

                # licenseData
                content["licenseData"]["type"] = 1
                content["licenseData"]["expirationDateUtc"] = "2099-01-01T00:00:00.0000000Z"
                content["licenseData"]["metadata"] = [
                    { "key": "Company", "value": "👀" },
                    { "key": "Name", "value": "🤷‍♂️" },
                    { "key": "EmailAddress", "value": "🥸" }
                ]

                # licenseStatus
                content["licenseStatus"]["occupiesSeat"] = True
                content["licenseStatus"]["usedSeatsCount"] = 1
                content["licenseStatus"]["featureSet"] = 3

                flow.response.text = json.dumps(content)
            
            elif current_url in ['https://api2.enscape3d.com/lic/api/session/start', 'https://api2.enscape3d.com/lic/api/session/continue', 'https://api2.enscape3d.com/lic/api/session/end']:
                content = json.loads(flow.response.get_text())

                # licenseStatus
                content["licenseStatus"]["occupiesSeat"] = True
                content["licenseStatus"]["usedSeatsCount"] = 1
                content["licenseStatus"]["featureSet"] = 3

                flow.response.text = json.dumps(content)


class ThreadedMitmProxy(threading.Thread):
    def __init__(self, user_addon: Callable, **options: Any) -> None:
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.master = Master(Options(), event_loop=self.loop)
        # replace the ScriptLoader with the user addon
        self.master.addons.add(
            *(
                user_addon() if isinstance(addon, script.ScriptLoader) else addon
                for addon in default_addons()
            )
        )
        # set the options after the addons since some options depend on addons
        self.master.options.update(**options)
        super().__init__()

    def run(self) -> None:
        self.loop.run_until_complete(self.master.run())

    def __enter__(self) -> Self:
        self.start()
        return self

    def __exit__(self, *_) -> None:
        self.master.shutdown()
        self.join()


if __name__ == "__main__":
    listen_host = "127.0.0.1"
    listen_port = 6666
    app_version = 1.0

    print(f"[Enscape Patcher v{app_version}]\n")

    with ThreadedMitmProxy(Addon, listen_host=listen_host, listen_port=listen_port):
        input(f"✅ Set Enscape proxy to {listen_host}:{listen_port}\n\nHit <Enter> to quit\n")
