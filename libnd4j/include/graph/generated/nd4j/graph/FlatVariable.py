# automatically generated by the FlatBuffers compiler, do not modify

# namespace: graph

import flatbuffers

class FlatVariable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFlatVariable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FlatVariable()
        x.Init(buf, n + offset)
        return x

    # FlatVariable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FlatVariable
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .IntPair import IntPair
            obj = IntPair()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FlatVariable
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # FlatVariable
    def Shape(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # FlatVariable
    def ShapeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FlatVariable
    def Ndarray(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .FlatArray import FlatArray
            obj = FlatArray()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FlatVariable
    def Device(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def FlatVariableStart(builder): builder.StartObject(5)
def FlatVariableAddId(builder, id): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)
def FlatVariableAddName(builder, name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def FlatVariableAddShape(builder, shape): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(shape), 0)
def FlatVariableStartShapeVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def FlatVariableAddNdarray(builder, ndarray): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(ndarray), 0)
def FlatVariableAddDevice(builder, device): builder.PrependInt32Slot(4, device, 0)
def FlatVariableEnd(builder): return builder.EndObject()
