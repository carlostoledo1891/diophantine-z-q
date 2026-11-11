"""Read-only quota probe for the approved private controller revision."""
import os
import sys

import runtime


def main(environment=None):
    env = os.environ if environment is None else environment
    config = runtime.read_protected_json(runtime.ROOT.resolve(), 'controller/config.json')
    runtime.exact(config, 'schema controller_repository controller_repository_id jobs',
                  'invalid controller config')
    runtime.require(config['schema'] == 'protocol-controller/v1' and
                    type(config['controller_repository_id']) is int and
                    config['controller_repository_id'] > 0, 'invalid controller identity')
    api = runtime.ControllerHTTPS(config['controller_repository'], env['GITHUB_TOKEN'])
    try:
        guard = runtime.RevisionGuard(api, config['controller_repository'],
            config['controller_repository_id'], env['PROTOCOL_APPROVED_SHA'], env)
        guard.check()
        return 0
    finally:
        api.diagnostics()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        print('Quota probe stopped: controller identity, revision or transport check failed.', file=sys.stderr)
        sys.exit(2)
