print("here")

DEVICE = 'gpu'
ENC_EMB_DIM = 256
DEC_EMB_DIM = 256
ENC_HID_DIM = 512
DEC_HID_DIM = 512
ENC_DROPOUT = 0.5
DEC_DROPOUT = 0.5

NUM_ITERS = 1000
BATCH_SIZE = 16
BEAM_SEARCH = False
PRINT_PER_ITER = 1
VALID_PER_ITER = 100
MAX_SAMPLE_VALID = 160

MAX_LR = 0.0003    # lr will inscrease from 2e-5 to MAX_LR in iter 0 -> iter NUM_ITERS * PCT_START, then decrease to 2e-5
PCT_START = 0.1

LOG = "/content/gdrive/MyDrive/ocr/Spelling_Correction_Vietnamese/log/loger_luong.log"
CHECKPOINT = '/content/gdrive/MyDrive/ocr/Spelling_Correction_Vietnamese/checkpoint/seq2seq_luong_checkpoint.pth'
EXPORT = '/content/gdrive/MyDrive/ocr/Spelling_Correction_Vietnamese/weights/seq2seq_luong.pth'

MAXLEN = 46
NGRAM = 5
alphabets = 'aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~ ]'
PERCENT_NOISE = 0.15 # 0 - 2 word in 5-grams
