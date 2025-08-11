from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import torchaudio
import tempfile
import os
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import logging
