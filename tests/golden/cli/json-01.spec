{
    "command": "fregot",
    "arguments": [
        "--format", "json",
        "eval", "data.fregot.tests.cli.invalid",
        "invalid.rego"
    ],
    "asserts": [
        {"exit_code": 1},
        {"stderr": "${SPEC_NAME}.stderr", "post_process": "prettify_json"}
    ]
}
