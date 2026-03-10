import sys
import types
import unittest


runpod_module = types.ModuleType("runpod")
serverless_module = types.ModuleType("runpod.serverless")
utils_module = types.ModuleType("runpod.serverless.utils")
rp_upload_module = types.ModuleType("runpod.serverless.utils.rp_upload")


def _fake_upload_image(*args, **kwargs):
    return "stub-upload"


rp_upload_module.upload_image = _fake_upload_image
utils_module.rp_upload = rp_upload_module
serverless_module.utils = utils_module
runpod_module.serverless = serverless_module

requests_module = types.ModuleType("requests")


class _FakeRequestException(Exception):
    pass


requests_module.RequestException = _FakeRequestException

websocket_module = types.ModuleType("websocket")

sys.modules.setdefault("runpod", runpod_module)
sys.modules.setdefault("runpod.serverless", serverless_module)
sys.modules.setdefault("runpod.serverless.utils", utils_module)
sys.modules.setdefault("runpod.serverless.utils.rp_upload", rp_upload_module)
sys.modules.setdefault("requests", requests_module)
sys.modules.setdefault("websocket", websocket_module)

import handler


class TestHandlerInputValidation(unittest.TestCase):
    def test_workflow_only_is_valid(self):
        validated, error = handler.validate_input({"workflow": {"foo": "bar"}})
        self.assertIsNone(error)
        self.assertEqual(validated["workflow"], {"foo": "bar"})
        self.assertIsNone(validated["images"])

    def test_missing_workflow_is_invalid(self):
        _, error = handler.validate_input({"images": []})
        self.assertEqual(error, "Missing 'workflow' parameter")

    def test_invalid_images_shape_is_rejected(self):
        _, error = handler.validate_input(
            {"workflow": {"foo": "bar"}, "images": [{"name": "x"}]}
        )
        self.assertEqual(
            error, "'images' must be a list of objects with 'name' and 'image' keys"
        )


if __name__ == "__main__":
    unittest.main()
